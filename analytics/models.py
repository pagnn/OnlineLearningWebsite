from django.db import models
from django.conf import settings
from courses.models import Course

# Create your models here.
class CourseViewEvent(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)
	course=models.ForeignKey(Course)
	views=models.IntegerField(default=0)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.views)


