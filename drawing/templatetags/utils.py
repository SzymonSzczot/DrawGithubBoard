from django import template

register = template.Library()


@register.filter
def as_range(value):
    return range(value)
