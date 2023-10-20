from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_Details
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels={
            'username':'Username',
            'email':'Email',
            'password1':'Password',
            'password2':'Confirm Password',
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Username '}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email '}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password '}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter your Password '}),
        }

class UserDetailsForm(forms.ModelForm):
    gen_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ) 
    class Meta:
        
        model = User_Details
        fields = ['name', 'phone', 'dob','gender', 'country', 'state', 'photo']
        labels={
              'name':'Name',
              'dob':'DOB',
              'phone':'Phone',
              'country':'Country',
              'state':'State',
              'gender':'Gender',
              'photo':'Profile Picture'
        }
        
        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
              'dob':forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'Enter your Date of Birth'}),
              'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Mobile Number'}),
              'country':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Nation'}),
              'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your State'}),
              'photo':forms.FileInput(attrs={'class':'form-control'}),
              'gender':forms.RadioSelect(attrs={'class':'form-check-input'})
              }
    gender = forms.ChoiceField(choices=gen_choices, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}))
class LoginForm(forms.Form):
    username=forms.CharField(label='Username',max_length=100,widget= forms.TextInput
                           (attrs={'placeholder':'Enter your username','class':'form-control'
                                 }))
    password=forms.CharField(label='Name',max_length=100,widget= forms.PasswordInput
                           (attrs={'placeholder':'Enter your password','class':'form-control'
                                 }))
