from django import forms
from .import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'body', 'slug', 'thumb']