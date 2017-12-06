from django.contrib import admin

# Register your models here.
from .models import Category
from .forms import CategoryAdminForm


class CategoryAdmin(admin.ModelAdmin):
	list_filter=['updated','timestamp']
	list_display=['title','updated','timestamp','order']
	readonly_fields=['updated','timestamp']
	search_fields=['title']
	list_editable=['order']
	form = CategoryAdminForm

admin.site.register(Category,CategoryAdmin)