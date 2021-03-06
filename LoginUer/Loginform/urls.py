from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup',views.index,name='register'),
    path('login',views.loginpage,name='login'),
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logoutuser,name='logout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)