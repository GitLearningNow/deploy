from django import template

register = template.Library()

@register.filter(name='cut')
def cut(full_value, str_to_remove):
    return full_value.replace(str_to_remove,'')
#register.filter('cut',cut)
