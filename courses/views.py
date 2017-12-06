from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,RedirectView
from django.db.models import Prefetch
from django.http import Http404
# Create your views here.
from .models import Course,Lecture,MyCourses
from .forms import CourseForm
from srvup.mixins import StaffMemberRequiredMxin
class CourseListView(ListView):
	def get_queryset(self):
		request=self.request
		query=request.GET.get('q')
		user=request.user
		qs=Course.objects.all()
		if query:
			qs=Course.objects.filter(title__icontains=query)
		if user.is_authenticated():
			qs=qs.owned(user)		
		return qs
class CourseCreateView(StaffMemberRequiredMxin,CreateView):
	model =Course
	form_class=CourseForm
	# success_url='/courses/'

	def form_valid(self,form):
		obj=form.save(commit=False)
		obj.user=self.request.user
		obj.save()
		return super(CourseCreateView,self).form_valid(form)

class CoursePurchaseView(LoginRequiredMixin,RedirectView):
	permanent=False
	def get_redirect_url(self,slug=None):
		request=self.request
		qs=Course.objects.filter(slug=slug).owned(request.user)
		if qs.exists():
			if request.user.is_authenticated():
				my_courses=MyCourses.objects.get(user=request.user)
				my_courses.courses.add(qs.first())
				return qs.first().get_absolute_url()	
			return qs.first().get_absolute_url()
		return '/courses/'
class CourseDetailView(DetailView):

	def get_object(self,*args,**kwargs):
		request=self.request
		slug=self.kwargs.get('slug')
		qs=Course.objects.filter(slug=slug).owned(request.user)
		if qs.exists():
			return qs.first()
		raise Http404

class LectureDetailView(DetailView):
	def get_object(self,*args,**kwargs):
		request=self.request
		cslug=self.kwargs.get('cslug')
		lslug=self.kwargs.get('lslug')
		obj=get_object_or_404(Lecture,slug=lslug,course__slug=cslug)
		return obj

class CourseUpdateView(StaffMemberRequiredMxin,UpdateView):
	model =Course
	form_class=CourseForm
class CourseDeleteView(StaffMemberRequiredMxin,DeleteView):
	queryset=Course.objects.all()
	success_url='/courses/'		


