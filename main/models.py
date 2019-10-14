from django.db import models
#import user method for django
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    '''
    avatar:to show in comment section
    bio: describe the account owner using text
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_pic = models.ImageField(default = 'default.jpg',upload_to = 'ProfilePIcture/')
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True, null = True)
    def __str__(self):
        return f'{self.user.username} Profile'


class Image(models.Model):

    '''
    uploader :user who has uploaded the image
    likes: number of likes per image
    caption : more info about the image
    image: the image itself
    '''
    image = models.ImageField(upload_to ='pictsagram/')
    caption = models.CharField(max_length=700)
    uploader_profile = models.ForeignKey(User, on_delete=models.CASCADE,null='True', blank=True)
    likes = models.ManyToManyField('Profile', default=False, blank=True, related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null= True)

    '''Method to filter database results'''
    def __str__(self):
        return self.caption





