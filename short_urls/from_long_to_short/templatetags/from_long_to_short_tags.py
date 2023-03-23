from django import template
from from_long_to_short.models import *

register = template.Library()

@register.simple_tag() # чтобы присвоить имя тега, нужно передать параметр name='tag_name', не забудь обращаться к тегу по новому имени
def get_shorts():
    return ShortURLs.objects.all()

@register.inclusion_tag('from_long_to_short/show_shorts.html')
def show_shorts():
    all = ShortURLs.objects.all()
    return {'all': all}