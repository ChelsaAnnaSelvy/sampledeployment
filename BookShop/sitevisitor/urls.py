from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home,inspirational,autobiography,signup_user,login_user

urlpatterns=[
    path('',home,name='home'),
    path('inspirational/',inspirational,name='inspirational'),
    path('autobiography/',autobiography,name='autobiography'),
    path('login/',login_user,name='login'),
    path('signup/',signup_user,name='register'),
    path('user_account/',include('useraccount.urls'))

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)