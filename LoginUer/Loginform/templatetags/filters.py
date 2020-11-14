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

def compare(value,element):
    if value == 1:
        return element
    else:
        return ""

def comparefilter(value, arg):
    if arg[0] == "shahzaib" and arg[1] == '12345':
        if value == 1:
            return arg[2]
        else:
            return ""
    else:
        return ""
     

  



register.filter('addition', addition)
register.filter('subtraction', subtraction)
register.filter('multiplication', multiplication)
register.filter('divide', divide)
register.filter('compare', compare)
register.filter('comparefilter', comparefilter)
