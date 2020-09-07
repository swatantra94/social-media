from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=1024)
    description = models.TextField()


    def __str__(self):
        return self.title

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post= models.ForeignKey('Post',on_delete=models.CASCADE)
    likes = models.BooleanField(default=0)

class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=256,null=True,blank=True)

    def __str__(self):
        return self.comment