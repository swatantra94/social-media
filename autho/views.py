from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from autho import forms
from django.http import HttpResponse,HttpResponseRedirect
import re

# Create your views here.

def login(request):
    form = forms.LoginForm()
    context = {
        "form":form
    }
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/auth/login/')
    return render(request,'auth/login.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')

def signup(request):
    form = forms.SignUpForm()
    error = ""
    context={
        "forms":form,
        "errors":error   
    }
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password=form.cleaned_data["confirm_password"]
            email = form.cleaned_data["email"]
            if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
                if password==confirm_password:
                    if User.objects.filter(username=username).exists():
                        error="username should be unique"
                        context={
                            "forms":form,
                            "errors":error
                        }
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password)
                        user.save()
                        return HttpResponseRedirect('/auth/login/')
                else:
                    error="password and confirm password should be match"
                    context={
                        "forms":form,
                        "errors":error
                    }
            else:
                error="Password should be atleast 8 and also contain a special, upper and lower class character "
                context={
                    "forms":form,
                    "errors":error
                }
    return render(request,'auth/signup.html',context)
