import random
import string
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.text import slugify

def random_string_generator(size=4,chars=string.ascii_lowercase+string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance,new_slug=None):
	if new_slug is not None:
		slug=new_slug
	else:
		slug=slugify(instance.title)
	klass=instance.__class__
	qs=klass.objects.filter(slug=slug)
	if qs.exists():
		new_slug='{slug}-{random_str}'.format(slug=slug,random_str=random_string_generator(size=4))
		return unique_slug_generator(instance,new_slug)
	else:
		return slug

def make_display_price(price):
	dollars=round(price,2)
	return "$%s%s"%(intcomma(int(dollars)),("%0.2f" % dollars)[-3:])