from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    dowload_slug = models.URLField(max_length=250)
    images = models.ImageField(upload_to='library_images', blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name