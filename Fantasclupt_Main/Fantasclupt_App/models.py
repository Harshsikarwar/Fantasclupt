from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Data(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    user_name=models.TextField(max_length=200, blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    otp=models.IntegerField(blank=True, null=True)
    package=models.TextField(blank=True, null=True)
    subscribe_date=models.DateField(blank=True, null=True)
    Expire_date=models.DateField(blank=True, null=True)
    verify=models.BooleanField(blank=True, null=True)