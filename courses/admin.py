from django.contrib import admin

# Register your models here.
from .models import Course,Lecture,MyCourses
from .forms import LectureAdminForm
class LectureInline(admin.TabularInline):
	model = Lecture
	form = LectureAdminForm
	prepopulated_fields={'slug':('title',)}
	extra=1

class CourseAdmin(admin.ModelAdmin):
	inlines=[LectureInline]
	list_filter=['updated','timestamp']
	list_display=['title','updated','timestamp','category','order']
	readonly_fields=['updated','timestamp']
	search_fields=['title','description']
	list_editable=['category','order']
	class Meta:
		model=Course



admin.site.register(Course,CourseAdmin)
admin.site.register(MyCourses)

