from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404
from .forms import CreateUserForm,Userupdateform,Userupdateprofile,Opps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views import View
# import django.views.generic.base import TemplateView

# Create your views here.

def index(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
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
    return render(request,'new.html',{'val1':10,'val2':2,'val3':5,'username':'Shahzaib','password':'12345','id':3})

class classbased(View):
    def get(self,request):
        form = Opps()
        return render(request,'opps.html',{'form':form})

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
    
            return render(request,'opps.html',{'form':form,'result':result})
        
  