from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key):
    """
    allows a version of the split function in templates
    """
    return value.split(key)
