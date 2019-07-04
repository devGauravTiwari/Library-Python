from django import template

register=template.Library()

@register.filter(name='replaceleadingslash')
def replaceleadingslash(value):
    return value.replace('/', '',1)
@register.filter(name='urlequate')
def urlequate(value,arg1):
    value=value.split('/').pop()
    return value==arg1
