# import requests
# import json

# def data(country):
#     if country is not None:
#         curData = requests('http://api.currencylayer.com/live?access_key=eb821c1dbf7ba857ccc0a40e3c342da5&currencies={}'.format(country))
#         Cdata = curData.text()
#         return Cdata
#     else:
#         curData = requests('http://api.currencylayer.com/live?access_key=eb821c1dbf7ba857ccc0a40e3c342da5&currencies=CAD')
#         Cdata = curData.text()
#         return Cdata
# r = requests.get('some url')
# data = r.text