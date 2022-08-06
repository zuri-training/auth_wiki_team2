from django.db import models
from django import forms
from PIL import Image
from accounts.models import MyUser


from django.conf import settings
from django.db import models

import uuid
import os

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profile_pics', filename)

def get_cover_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('cover_pics', filename)


class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='first_name', max_length=150, default=0000)
    middle_name = models.CharField(verbose_name='middle_name', max_length=150, default=0000)
    last_name = models.CharField(verbose_name='last_name', max_length=150, default=0000)
    position = models.CharField(verbose_name='position', max_length=300,  default='')
    image = models.FileField(upload_to=get_image_path, null=True, blank=True, default='default.jpg')
    cover = models.FileField(upload_to=get_cover_path, null=True, blank=True, default='default.jpg')
    bio = models.TextField(verbose_name='bio', max_length=500,  default='')
    # portfolio = models.TextField(verbose_name='portfolio', max_length=350,  default='')
    city = models.CharField(verbose_name='city', max_length=30, default='')
    country = models.CharField(verbose_name='country', max_length=50, default='')
    website  = models.URLField(max_length=500, null=True, blank=True,)
    facebook = models.URLField(max_length=500, null=True, blank=True,)
    twitter = models.URLField(max_length=500, null=True, blank=True,)
    instagram = models.URLField(max_length=500, null=True, blank=True,)
    github = models.URLField(max_length=500, null=True, blank=True,)



    def __str__(self):
        return f'{self.user.username} User Profile'

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
