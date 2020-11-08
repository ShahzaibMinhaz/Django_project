from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
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
            return redirect('/')
        else :
            error = form.errors
            print(error.as_data)
            messages.info(request, error)
            # return redirect('/')
            # return render(request,'index.html',{'form':form,'error':error})

    form = CreateUserForm()
    return render(request,'index.html',{'form':form})

def loginpage(request):
    if request.method == 'POST':
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

def home(request):
    return render(request,'home.html')
