import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.CharField(max_length=200)
    profileimg=models.ImageField(upload_to='profile_image',default='default-avatar-icon-of-social-media-user-vector.jpg')
    loc=models.CharField(max_length=15,default='bangladesh')
    

class POST(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='POSTIMAGE/')
    Captions=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    like_count=models.PositiveIntegerField(default=0)
    

class img(models.Model):
    images=models.ImageField(upload_to='tryTheenv')
    create_at=models.DateTimeField(auto_now=True)
    
class Like_Post(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=50)
def __str__(self):
    return self.username


class FollowerCount(models.Model):
    Follower=models.CharField(max_length=25)
    user=models.CharField(max_length=25)
def __str__(self):
    return self.user