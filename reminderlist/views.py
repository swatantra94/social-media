from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from reminderlist import models,forms
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
            form = form.save()
            return HttpResponseRedirect('/todo/')
    return render(request,'social/create.html',context)
    
@login_required(login_url='/auth/login')
def delete(request,pk):
    models.Post.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/todo/')

@login_required(login_url='/auth/login')
def wall(request):
    posts = models.Post.objects.all()
    a=[]
    for post in posts:
        if post.user.id==request.user.id:
            a.append(post)
    context={
        "a":a
    }
    return render(request,'social/wall.html',context)


def comment(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect('/todo/')
    else:
        form = forms.CommentForm()
    return render(request, 'social/comment.html', {'form': form})