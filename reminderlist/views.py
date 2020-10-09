from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from reminderlist import models,forms
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from reminderlist import forms
from django.contrib.auth import login as auth_login
import re

# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    posts = models.Post.objects.all()
    context = {
        "posts":posts,
    }
    return render(request,'social/index.html',context)

@login_required(login_url='/auth/login')
def activity(request,pk):
    activity = get_object_or_404(models.Post,pk=pk)
    context = {
        "activity":activity
    }
    return render(request, 'social/activity.html',context)
    
@login_required(login_url='/auth/login')
def create(request):
    form = forms.PostForms()
    context={
        "form":form
    }
    if request.method=="POST":
        form = forms.PostForms(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'social/create.html',context)
    
@login_required(login_url='/auth/login')
def delete(request,pk):
    models.Post.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/auth/login')
def wall(request):
    posts = models.Post.objects.all()
    a=[]
    for post in posts:
        if post.user.id==request.user.id:
            a.append(post)
    if len(a)>0:
        context={
            "a":a
        }
    else:
        b="Oops! there is nothing to show"
        context={
            "a":a,
            "b":b
        }       
    return render(request,'social/wall.html',context)

@login_required(login_url='/auth/login')
def comment(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.CommentForm()
    return render(request, 'social/comment.html', {'form': form})


def like(request,pk):
    a=request.POST.get('post_id')
    user=request.user
    post = get_object_or_404(models.Post,id=request.POST.get('post_id'))
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return HttpResponseRedirect('/')


@login_required(login_url='/auth/login')
def friend_post(request):
    a=request.user
    friendIds = [ friend.friend2.id for friend in  models.Friend.objects.filter(friend1 = request.user) ]
    friendIds = friendIds + [ friend.friend1.id for friend in  models.Friend.objects.filter(friend2 = request.user) ]
    a=models.Post.objects.filter(user__in = friendIds)
    if len(a)>0:
        context = {
            "a":a,
        }
    else:
        b = "Oops! your friends didn't post anything or you don't have any friends"
        context = {
            "a":a,
            "b":b
        }
    return render(request,'social/friend_post.html',context)

@login_required(login_url='/auth/login')
def change_password(request):
    form = forms.ChangePasswordForm()
    context = {
        "form":form,
    }
    a = request.user
    if request.method=="POST":
        form = forms.ChangePasswordForm(request.POST)
        if form.is_valid():
            a = request.user
            password = form.cleaned_data["old_password"]
            new_password = form.cleaned_data["new_password"]
            confirm_new_password=form.cleaned_data["confirm_new_password"]
            user = authenticate(request,username=a, password=password)
            if user is not None:
                if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', new_password):
                    if new_password==confirm_new_password:
                        u = User.objects.get(username=a)
                        u.set_password(new_password)
                        u.save()
                        user = authenticate(request,username=a, password=new_password)
                        auth_login(request,user)
                        return HttpResponseRedirect('/')
                    else:
                        context = {
                            "form":form,
                            "b":"your new password and confirm new password should be match"
                        }
                else:
                    context = {
                            "form":form,
                            "b":"New Password should be atleast 8 and also contain a special, upper and lower class character"
                    }
            else:
                context = {
                            "form":form,
                            "b":"please enter correct password"
                }
    return render(request,'social/change_password.html',context)