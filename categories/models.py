from django.db import models
from courses.fields import PositionField
from srvup.utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.core.urlresolvers import reverse
from django.db.models import Prefetch
from django.db.models import Count

from videos.models import Video
# Create your models here.


class CategoryQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

class CategoryManager(models.Manager):
	def get_queryset(self):
		return CategoryQuerySet(self.model,self._db)
	def all(self):
		return self.get_queryset().all(
			).active().annotate(
			courses_length=Count('primary_category',distinct=True)+Count('secondary_category',distinct=True)
			).prefetch_related('primary_category')


class Category(models.Model):
	title     	=models.CharField(max_length=120)
	slug        =models.SlugField(blank=True)
	video       =models.ForeignKey(Video,null=True,blank=True)
	order       =PositionField(blank=True)
	description =models.CharField(max_length=120)
	active      =models.BooleanField(default=True)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)	


	objects     =CategoryManager()
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('categories:detail',kwargs={'slug':self.slug})
def pre_save_category_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=unique_slug_generator(instance)
pre_save.connect(pre_save_category_receiver,sender=Category)