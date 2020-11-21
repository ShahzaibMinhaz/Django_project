from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404,JsonResponse
from .forms import CreateUserForm,Userupdateform,Userupdateprofile,Opps,customformajax,Invoice_details
from .models import itemdetails,invoiceheader,Person_details
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.db import transaction
from . import signals
from django.views import View
import requests
import json
# import django.views.generic.base import TemplateView
# from .Apitest import data

# Create your views here.

def index(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            print(username)
            form.save()
            messages.SUCCESS = (request, 'Acount Created')
            print('user created')
            return redirect('/login')
        else :
            error = form.errors
            print(error.as_data)
            messages.info(request, error)
            # return redirect('/')
            # return render(request,'index.html',{'form':form,'error':error})

    form = CreateUserForm()
    return render(request,'index.html',{'form':form})

def loginpage(request):
    '''
    this function is of about Login page
    '''
    if request.method == 'POST':
        '''
        this block will check the POST request
        '''
        # path = request.path
        print(request.POST['username'])
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')
            # return render(request,'login.html')

    else:
        print('No Post request')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')       

@login_required
def home(request):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request,'home.html')

@login_required
def profile(request):
    userform = Userupdateform()
    userprofile = Userupdateprofile()
    context = {
        'user': Userupdateform,
        "profile": Userupdateprofile
    }
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request,'profile.html',context)

def http(request):
    if id is None:
        pass
    else :
        raise Http404   ("Page does not exist")
    
def comments(request):
    page_number = 45 
    return render('','profile.html')  

    # return HttpResponse('<h1>hello World</h1>')

def opps(request):
    # if request.method == 'POST':
    #     form = Opps(request.POST)
    #     print(request.POST)
    #     if form.is_valid():
    #         sign = form.cleaned_data['Operation']
    #         value1 = form.cleaned_data['value1']
    #         value2 = form.cleaned_data['value2']
    #         if sign == '+':
    #             result = (value1 + value2)
    #         else:
    #             result = (value1 - value2)
    #         # str(result)
    #         # print(result)
    
    #         return render(request,'opps.html',{'form':form,'result':result})
    # form = Opps()
    
    return render(request,'opps.html',{'val1':10,'val2':2,'val3':5})
    
def new(request):
    data = ['shahzaib','12345','developer']
    return render(request,'new.html',{'val1':10,'val2':2,'val3':5,'data':data,'id':1})

class classbased(View):
    template_name = 'opps.html'
    def get(self,request):
        form = Opps()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = Opps(request.POST)
        if form.is_valid():
            sign = form.cleaned_data['Operation']
            value1 = form.cleaned_data['value1']
            value2 = form.cleaned_data['value2']
            if sign == '+':
                result = (value1 + value2)
            else:
                result = (value1 - value2)
            # str(result)
            # print(result)
    
            return render(request,self.template_name,{'form':form,'result':result})

def apirequest(request):
    news_data = requests.get('http://data.fixer.io/api/latest?access_key=23f15347a193045a1ab47e0eb94d0a86')
    '''countryname return all countries name'''
    countryname = news_data.json()['rates'].keys()
    if request.method == 'POST':
        currency = request.POST['country']
        try:
            # value = request.POST['value']
            # print(request.POST['country'])
            # print(request.POST['country'])
            country_name = currency
            '''country_name will give countryname to url to fetch exchange rate'''
            news_data = requests.get('http://api.currencylayer.com/live?access_key=eb821c1dbf7ba857ccc0a40e3c342da5&currencies={}'.format(country_name))
            # values = data('PKR')
            # print(values)
            currencyvalue = news_data.json()['quotes']['USD{}'.format(country_name)]
            return render(request,'currency.html',{'countryname':countryname,'currencyvalue':currencyvalue,'country_name':country_name})
        except:
            print("country name not mentioned")
    return render(request,'currency.html',{'countryname':countryname})
    
    


# class currechanger(View):
#     template_name = 'currency.html'
#     def get(self,request):
#         form = curr()
#         return render(request,self.template_name,{'form':form})

#     # def post(self,request):
        # form = curr(request.POST)
        # if form.is_valid():
        #     sign = form.cleaned_data['Operation']
        #     value1 = form.cleaned_data['value1']
        #     value2 = form.cleaned_data['value2']
        #     if sign == '+':
        #         result = (value1 + value2)
        #     else:
        #         result = (value1 - value2)
        #     str(result)
        #     print(result)


def getcurrency(request):
    if request.method == 'POST':
        print('In getcurrency post request')
        currency = request.POST['value']
        # print('currency = ',currency)
        try:
            country_name = currency
            '''country_name will give countryname to url to fetch exchange rate'''
            news_data = requests.get('http://api.currencylayer.com/live?access_key=eb821c1dbf7ba857ccc0a40e3c342da5&currencies={}'.format(country_name))
            # values = data('PKR')
            # print(values)
            currencyvalue = news_data.json()['quotes']['USD{}'.format(country_name)]
            return HttpResponse(currencyvalue)
        except:
            print("country name not mentioned")
            return HttpResponse('false')

def djangoform(request):
    form = customformajax()
    return render(request,'customformajax.html',{'form':form})

def getdata(request):
    Name = request.POST['name']
    Email = request.POST['email']
    context = {'name':Name,'email':Email} 
    return JsonResponse(context)


def setsessions(request):
    request.session['name'] = 'Shahzaib'
    return render(request,'sessions.html')

def getsessions(request):
    name = request.session['name']
    return render(request,'sessions.html',{'name':name})

def delsessions(request):
    if request.session:
        del request.session['name']
    return render(request,'sessions.html')

def requestsessions(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        print('Permission')
    else:
        request.session.set_test_cookie()
        messages.error(request, 'Please enable cookie')
        print('enable permission')
    return render(request, 'sessions.html')

def invoice(request):
    form = Invoice_details()
    return render(request,'Invoice.html',{'form':form})

def submitinvoicedata(request):

    # get data from ajax request 
    table_Data = json.loads(request.POST['table_Data'])
    total_Price = request.POST['total_Price']
    print(table_Data)
    if request.user.is_authenticated:
        try:
            with transaction.atomic():
                # to save data in invoice header
                invoice = invoiceheader.objects.create(Name=request.user.username,Total_Price=total_Price)
                invoice.save()
                id = invoice.id

                # getting invoice id 
                invoice_id = invoiceheader.objects.get(id=id)
                signals.Itemdetailssave.send(sender=None,tabledata=table_Data,Invoice=invoice_id,created=True)

                # # for to save individual item data in table 
                # for i in range(len(table_Data)):
                #     # print('entry No ',i)
                #     productName = table_Data[i]['productName']
                #     productQuantity = table_Data[i]['productQuantity']
                #     productPrice = table_Data[i]['productPrice']
                #     print('Invoice ID',type(id))
                #     item_details = itemdetails.objects.create(Item_Name=productName,Item_quentity=productQuantity,Item_Price=productPrice,Invoice_header=invoice_id)
                #     item_details.save()


                return HttpResponse('Item Sucessfully saved')
        except DatabaseError:
            print(DatabaseError)
            return HttpResponse("Database error")
    return HttpResponse('User is not logged in')

def modelManager(request):
    people = Person_details.personorder.get_person_by_id(1,3)
    return render(request,'modelmanager.html',{'people':people})