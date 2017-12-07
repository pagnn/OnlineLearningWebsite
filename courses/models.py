from django.db import models
from django.conf import settings
from django.utils.text import slugify
from srvup.utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.core.urlresolvers import reverse
from django.db.models import Prefetch

# Create your models here.

from videos.models import Video
from .fields import PositionField
from srvup.utils import make_display_price
from categories.models import Category


class MyCourses(models.Model):
	user        =models.OneToOneField(settings.AUTH_USER_MODEL)
	courses     =models.ManyToManyField('Course',blank=True,related_name='owned')
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.courses.all().count())
	class Meta:
		verbose_name='My courses'
		verbose_name_plural='My courses'

def post_save_user_receiver(sender,instance,created,*args,**kwargs):
	if created:
		MyCourses.objects.get_or_create(user=instance)


post_save.connect(post_save_user_receiver,sender=settings.AUTH_USER_MODEL)


class CourseQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)
	def lectures(self):
		return self.prefetch_related('lecture_set')
	def owned(self,user):
		if user.is_authenticated():
			qs=MyCourses.objects.filter(user=user)
		else:
			qs=MyCourses.objects.none()
		return self.prefetch_related(Prefetch('owned',
										queryset=qs,
										to_attr='is_owner'
				))
	def featured(self):
		return self.filter(category__title__icontains='featured')
class CourseManager(models.Manager):
	def get_queryset(self):
		return CourseQuerySet(self.model,using=self._db)
	def all(self):
		return self.get_queryset().all().active()
	def owned(self,user):
		return self.get_queryset().owned(self,user)
	def lectures(self):
		return self.get_queryset().lectures()
	def featured(self):
		return self.get_queryset().featured()
def handle_upload(instance,filename):
	if instance.slug:
		return "%s/images/%s"%(instance.slug,filename)
	return "unknown/images/%s"%(filename)
class Course(models.Model):
	user        =models.ForeignKey(settings.AUTH_USER_MODEL)
	title     	=models.CharField(max_length=120)
	image       =models.ImageField(upload_to=handle_upload,height_field='image_height',width_field='image_width',blank=True,null=True)
	image_height = models.IntegerField(null=True,blank=True)
	image_width = models.IntegerField(null=True,blank=True)
	category    =models.ForeignKey(Category,related_name='primary_category',null=True,blank=True)
	secondary   =models.ManyToManyField(Category,related_name='secondary_category',blank=True)
	order       =PositionField(collection='category')
	slug        =models.SlugField(blank=True)
	description =models.CharField(max_length=120)
	price       =models.DecimalField(decimal_places=2,max_digits=20)
	active      =models.BooleanField(default=True)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	objects     =CourseManager()

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('courses:detail',kwargs={'slug':self.slug})
	def display_price(self):
		return make_display_price(self.price)
	def get_purchase_url(self):
		return reverse('courses:purchase',kwargs={'slug':self.slug})
def pre_save_course_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:

		instance.slug=unique_slug_generator(instance)
pre_save.connect(pre_save_course_receiver,sender=Course)

def post_save_course_receiver(sender,instance,created,*args,**kwargs):
	if not instance.category in instance.secondary.all():
		instance.secondary.add(instance.category)
post_save.connect(post_save_course_receiver,sender=Course)

#foreign key limit_choices_to={'lecture__isnull':False,'title__icontains':'something'}
class Lecture(models.Model):
	course 		=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
	video       =models.ForeignKey(Video,on_delete=models.SET_NULL,null=True)
	title     	=models.CharField(max_length=120)
	order       =PositionField(collection='course')
	slug        =models.SlugField(blank=True)
	free        = models.BooleanField(default=False)
	description =models.CharField(max_length=120,blank=True)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
	class Meta:
		unique_together=(('slug','course'),)
		ordering=['order','title']
	def get_absolute_url(self):
		return reverse('courses:lecture-detail',kwargs={'cslug':self.course.slug,'lslug':self.slug})