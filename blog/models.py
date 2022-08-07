from django.db import models
from accounts.models import MyUser


import uuid
import os


def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('blog_pics', filename)


# # Create your models here.
class Blog(models.Model): 

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.FileField(upload_to=get_image_path, null=True, blank=True, default='default.jpg')
    author = models.ForeignKey(MyUser, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:60]+'...'

