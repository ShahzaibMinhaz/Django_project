from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup',views.index,name='register'),
    path('login',views.loginpage,name='login'),
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logoutuser,name='logout'),
    path('classview',views.classbased.as_view()),
    # path('template',views.Tempal)
    path('new',views.new,name='new'),
    path('cur',views.apirequest),
    path('setsessions',views.setsessions),
    path('getsessions',views.getsessions),
    path('delsessions',views.delsessions),
    path('requestsessions',views.requestsessions),
    path('invoice',views.invoice),


    # with AJAX request
    path('customformajax',views.djangoform),
    path('getcurrency/',views.getcurrency),
    path('getdata/',views.getdata)
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)