from django import forms
from reminderlist import models

class PostForms(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']

class FriendForm(forms.ModelForm):
    class Meta:
        model = models.Friend
        fields = ['friend2']