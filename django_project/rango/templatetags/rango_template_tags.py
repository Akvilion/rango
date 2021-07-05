from django import template
from ..models import Category

register = template.library()

@register.inclusion_tag('rango/categories.html')
def get_category_list():
    return {'categories': Category.objects.all()}

