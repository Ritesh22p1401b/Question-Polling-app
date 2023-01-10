from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username=models.CharField(verbose_name='Username',max_length=256,unique=True)
    first_name=models.CharField(verbose_name='First Name',max_length=100)
    last_name=models.CharField(verbose_name='Last Name',max_length=100)
    email=models.EmailField(verbose_name='E-mail',max_length=256,unique=True)
    phone_number=PhoneNumberField(null=False,unique=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone_number','first_name','last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name
