from django.shortcuts import render
from django.views.generic import View
from django.db.models import Prefetch

from courses.models import Course
from analytics.models import CourseViewEvent

class HomeView(View):
	def get(self,request,*args,**kwargs):
		courses_qs=Course.objects.lectures().owned(request.user)
		featured_qs=courses_qs.featured().distinct().order_by('?')[:6]
		event_views=CourseViewEvent.objects.all().prefetch_related('course')
		if request.user.is_authenticated():
			event_views=event_views.filter(user=request.user)
		event_views=event_views.order_by('views')[:6]
		ids_qs=[x.course.id for x in event_views]
		rec_qs=courses_qs.filter(id__in=ids_qs).order_by('?')
		context={
			'featured_qs':featured_qs,
			'rec_qs':rec_qs,
		}

		return render(request,'home.html',context)