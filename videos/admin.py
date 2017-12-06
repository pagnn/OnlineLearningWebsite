from django.contrib import admin
from .models import Video
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
	list_filter=['updated','timestamp']
	list_display=['title','timestamp','updated']
	readonly_fields=['timestamp','updated']
	search_fields=['title']
	class Meta:
		model=Video

admin.site.register(Video,VideoAdmin)