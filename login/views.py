from django.shortcuts import render, redirect
from .forms import LoginForm
from home.views import *


# Create your views here.


def login(request):
    if "result" in request.COOKIES.keys():
        if request.COOKIES.get("result") != "":
            return redirect('/home/dashboard/')
    return render(request, "login/login.html")
