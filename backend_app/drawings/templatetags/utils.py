from django import template

register = template.Library()


@register.filter
def as_range(start, end):
    return range(int(start), int(end))


@register.filter
def concat(str1, str2):
    return str(str1) + str(str2)
