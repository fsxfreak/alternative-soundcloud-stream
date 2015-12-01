from django import template

register = template.Library()

@register.filter(name='next1')
def next1():
    
@register.filter(name='next2')
def next2():
@register.filter(name='next3')
def next3():
