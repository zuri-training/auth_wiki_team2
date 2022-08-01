from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    email = models.CharField(max_length=20)
    created_at = models.DateField( default = datetime.now, blank = True)
    updated_at = models.DateField(default= datetime.now, blank = True)
