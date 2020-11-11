from django import template

register = template.Library()
def addition(value,element):
    # print(value+element)
    return (value+element)

def subtraction(value,element):
    # print(value+element)
    return (value-element)

def multiplication(value,element):
    # print(value*element)
    return (value*element)

def divide(value,element):
    # print(value/element)
    return (value/element)

register.filter('addition', addition)
register.filter('subtraction', subtraction)
register.filter('multiplication', multiplication)
register.filter('divide', divide)