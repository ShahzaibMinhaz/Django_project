from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.core.exceptions import PermissionDenied


def permission_denied_view(request):
    raise PermissionDenied()

urlpatterns = [
    path('signup',views.index,name='register'),
    path('login',views.loginpage,name='login'),
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logoutuser,name='logout'), 
    path('http',permission_denied_view),
    path('httpreq',views.http),
    re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', views.comments),
    path('Opps',views.opps),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)