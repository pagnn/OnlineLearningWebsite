from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models import Q
from srvup.utils import unique_slug_generator
# Create your models here.
from django.db.models.signals import pre_save


class VideoQuerySet(models.query.QuerySet):
	def unused(self):
		return self.filter(Q(lecture__isnull=True)&Q(category__isnull=True))

class VideoManager(models.Manager):
	def get_queryset(self):
		return VideoQuerySet(self.model,self._db)
	def unused(self):
		return self.get_queryset().unused()


class Video(models.Model):
	title     	=models.CharField(max_length=120)
	slug        =models.SlugField(blank=True)
	embed_code  =models.TextField()
	free		=models.BooleanField(default=True)
	member_required =models.BooleanField(default=False)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	objects     =VideoManager()
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('videos:detail',kwargs={'slug':self.slug})

def pre_save_video_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=unique_slug_generator(instance)

pre_save.connect(pre_save_video_receiver,sender=Video)