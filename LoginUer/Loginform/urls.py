from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('login',views.loginpage,name='login'),
    path('home',views.home,name='home')
]