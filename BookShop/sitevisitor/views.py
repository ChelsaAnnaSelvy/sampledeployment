from django.shortcuts import render,redirect
from .models import Category,Products,User_Details,User
from django.contrib.auth.models import User
from .forms import UserDetailsForm,UserForm,LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    products=Products.objects.all()
    return render(request,'home.html',{'products':products})
def inspirational(request):
    return render(request,'inspirational.html')
def autobiography(request):
    return render(request,'autobiography.html')
def login_user(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('userhome')
        else:
            form=LoginForm()
            error_message='Invalid Username or Password'
            return render(request,'login.html',{'form':form,'error':error_message})
            error_message='Invalid Username or Password'
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
def signup_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='user')
        user_details_form = UserDetailsForm(request.POST,request.FILES, prefix='user_details')

        if user_details_form.is_valid() and  user_form.is_valid():
            user = user_form.save()
            user_details = user_details_form.save(commit=False)
            user_details.email = user.email  # Set the email from the User model
            user_details.user_cred = user
            user_details.save()
            return redirect('home')
    else:
        user_form = UserForm(prefix='user')
        user_details_form = UserDetailsForm(prefix='user_details')

    return render(request, 'register.html', {
        'form1': user_form,
        'form': user_details_form,
    })