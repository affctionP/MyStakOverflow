
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.

class USER (AbstractUser):
    name=models.CharField(max_length=30,default="کاربر" , null=True)
    
    username=None
    email =models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
    
    def __str__(self):
        return self.email