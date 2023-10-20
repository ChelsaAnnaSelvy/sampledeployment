from django.contrib import admin
from django.contrib.auth.models import User
from .models import Products,Category,User_Details

# Register your models here.
admin.site.register(Category)
admin.site.register(User_Details)
admin.site.register(Products)