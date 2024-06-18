from django.shortcuts import render
import os

dic=os.path.dirname(__file__)
dic.replace("\\","\\\\")

# Create your views here.

def sing_up_page(request):
    return render(request, dic+"\\templates\\sing-up.html")