from django.db import models
from django.contrib.auth.models import User
# Create your models here.

   
class User_Details(models.Model):
    user_cred=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=100,unique=True)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='user/',blank=True,null=True)
    gender=models.CharField(max_length=100)
    dob=models.DateField()

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
class Products(models.Model):
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    dop=models.DateField()
    cover_photo=models.ImageField(upload_to='products',blank=True,null=True)
    rate=models.DecimalField(max_digits=7,decimal_places=2)
    stock=models.IntegerField()
    def __str__(self):
        return self.title
    