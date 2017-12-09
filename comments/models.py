from django.db import models
from django.conf import settings
# Create your models here.
class Comment(models.Model):
	url = models.URLField()
	content = models.CharField(max_length=120)
	user =models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)
	allow_annon=models.BooleanField(default=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.url

	@property
	def owner(self):
		return self.user