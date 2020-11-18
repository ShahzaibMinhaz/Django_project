import datetime

def number(request):
    result = 12 + 16
    return {'result':result}

def date(request):
    date = datetime.datetime.today()
    return {'date':date}