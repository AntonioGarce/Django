from django import template
from loguru import logger

register = template.Library()


# views.py
@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)


@register.filter(name='divide')
def divide(value, arg):
    try:
        return round(float(value) / float(arg), 1)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter(name='multi')
def divide(value, arg):
    try:
        return round(float(value) * float(arg), 1)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter('edit')
def edit(value: str):
    return value.replace("\n", "<br>")
