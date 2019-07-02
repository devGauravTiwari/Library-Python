from django import template

register=template.Library()

@register.filter(name='replaceleadingslash')
def replaceleadingslash(value):
    return value.replace('/', '',1)
@register.filter(name='urlequate')
def urlequate(value,args):
    value=value.replace('/','',1)
    return value==args
