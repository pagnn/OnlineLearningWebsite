from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
# Create your views here.
from courses.models import Course,Lecture 
from categories.models import Category

class SearchView(View):
	def get(self,request,*args,**kwargs):
		query=request.GET.get('q')
		qs=None
		c_qs=None
		l_qs=None
		if query:
			query_lookup=Q(title__icontains=query)\
						|Q(description__icontains=query)\
						|Q(category__title__icontains=query)\
						|Q(category__description__icontains=query)\
						|Q(lecture__title__icontains=query)
			qs=Course.objects.filter(query_lookup).lectures().distinct()
			qs_ids=[x.id for x in qs]
			c_lookup=Q(primary_category__in=qs_ids) | Q(secondary_category__in=qs_ids)
			c_qs=Category.objects.filter(c_lookup).distinct()
		context={
			'qs':qs,
			'c_qs':c_qs,

		}
		return render(request,'search/default.html',context)
