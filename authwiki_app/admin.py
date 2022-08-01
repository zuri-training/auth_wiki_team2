from django.contrib import admin
from authwiki_app.models import Contact, Profile

# Register your models here.
admin.site.register(Contact, Profile)
