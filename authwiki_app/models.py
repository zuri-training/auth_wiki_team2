from django.db import models
from datetime import datetime


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class otp(models.Model):
    user = models.OneToOneField('self', default=None, null=True, on_delete=models.CASCADE)
    hashed = models.CharField(default = "", max_length=4)
    created_at = models.DateField( default = datetime.now, blank = True)
    updated_at = models.DateField(default= datetime.now, blank = True)
    expire_time = models.TimeField(default = datetime.now, blank = True, max_length=20)
    expire_date = models.TimeField(default= datetime.now, blank = True, max_length=20)

