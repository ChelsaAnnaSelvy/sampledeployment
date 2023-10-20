from django.shortcuts import render,redirect
from django.contrib.auth import logout
from sitevisitor.models import User,User_Details
# Create your views here.
def home(request):
    try:
        user=request.user.email
        person_details = User.objects.filter(email=user)   
        det2=User_Details.objects.filter(email=user)

        return render(request,'user_home.html',{'user':person_details,'profile':det2})
    except: 
        return redirect('home')
def logout_user(request):
    logout(request)
    return redirect('login')

    