from . import views
from django.urls import  path

urlpatterns = [
   
    path('home/',views.home,name='userhome'),
    path('logout/',views.logout_user,name='logout'),
    
]