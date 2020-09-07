from django import forms
from reminderlist import models

class PostForms(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']