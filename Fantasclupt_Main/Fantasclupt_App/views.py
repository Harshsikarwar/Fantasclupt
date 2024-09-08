from django.shortcuts import render, redirect
import os
import random
from django.core.mail import send_mail
from .models import*
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

dic=os.path.dirname(__file__)
dic.replace("\\","\\\\")

# Create your views here.

def sign_up_page(request):
    if request.method == "POST":
        user=request.POST.get("user")
        email=request.POST.get("email")
        password=request.POST.get("password")

        user_model=User.objects.all()
        user_data=User_Data.objects.all()

        check_exists=user_data.filter(email=email)

        if check_exists.exists():
            messages.info(request,"Already Exists")
            return redirect("/Fantasclupt/sign-up/")

        user_model=User.objects.create(username=email)
        user_data=User_Data.objects.create(user_name=user,email=email, verify=False)
        
        user_model.set_password(password)
        user_model.save()
        user_data.save()

        auth=authenticate(request, username=email, password=password)
        login(request,auth)

        return redirect("/Fantasclupt/home/")
    return render(request, dic+"\\templates\\sign-up.html")

def sign_in_page(request):
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        user_model=User.objects.all()
        user_data=User_Data.objects.all()

        check_exists=user_model.filter(username=email)

        if not check_exists.exists():
            messages.info(request,"User Not Exists")
            return redirect("/Fantasclupt/sign-in/")
        
        auth=authenticate(request, username=email, password=password)
        if auth == None:
            messages.info(request,"Invalid Password/Email")
            return redirect("/Fantasclupt/sign-in/")

        login(request,auth)

        return redirect("/Fantasclupt/home/")
    return render(request, dic+"\\templates\\sign-in.html")

def home_page(request):
    return render(request, dic+"\\templates\\home.html")