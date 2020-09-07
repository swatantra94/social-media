from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from autho import forms
from django.http import HttpResponse,HttpResponseRedirect

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
                return HttpResponseRedirect('')
            else:
                return HttpResponseRedirect('/auth/login/')
    return render(request,'auth/login.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')

def signup(request):
    form = forms.SignUpForm()
    context={
        "form":form
    }
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password=form.cleaned_data["confirm_password"]
            email = form.cleaned_data["email"]
            if password==confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'username should be unique')
                    return HttpResponseRedirect('/auth/signup/')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return HttpResponseRedirect('/auth/login/')
            else:
                messages.info(request,'pasword should be mathed')
                return HttpResponseRedirect('/auth/signup/')

    return render(request,'auth/signup.html',context)
