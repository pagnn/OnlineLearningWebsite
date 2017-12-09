from django import template

register=template.Library()

from comments.models import Comment 

@register.inclusion_tag('comments/snippets/load-comments.html')
def load_comments(url):
	qs=Comment.objects.filter(url=url)
	return {'comments':qs}
