from django.db import models
#import user method for django
from django.contrib.auth.models import User



class Profile(models.Model):
    '''
    avatar:to show in comment section
    bio: describe the account owner using text
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_pic = models.ImageField(default = 'default.jpg',upload_to = 'ProfilePIcture/')
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.CharField(max_length=30)

    def __str__(self):
        return self.Profile.user





