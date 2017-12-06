from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
# Create your views here.
from .models import Video
from .forms import VideoForm
from srvup.mixins import MemberRequiredMixin,StaffMemberRequiredMxin
class VideoListView(ListView):
	def get_queryset(self):
		request=self.request
		query=request.GET.get('q')
		if query:
			qs=Video.objects.filter(title__icontains=query)
		else:
			qs=Video.objects.all()
		return qs
class VideoCreateView(StaffMemberRequiredMxin,CreateView):
	model =Video
	form_class=VideoForm

class VideoDetailView(MemberRequiredMixin,DetailView):

	def get_object(self,*args,**kwargs):
		request=self.request
		slug=self.kwargs.get('slug')
		video_obj=get_object_or_404(Video,slug=slug)
		return video_obj
class VideoUpdateView(StaffMemberRequiredMxin,UpdateView):
	model =Video
	form_class=VideoForm
class VideoDeleteView(StaffMemberRequiredMxin,DeleteView):
	queryset=Video.objects.all()
	success_url='/videos/'		

