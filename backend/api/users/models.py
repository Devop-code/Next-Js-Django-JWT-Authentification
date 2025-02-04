from django.db import models
from .manage import CustomUserManager
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS=[]
    
    objects = CustomUserManager()
    