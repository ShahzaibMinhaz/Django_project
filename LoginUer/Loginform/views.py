from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm,Userupdateform,Userupdateprofile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

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