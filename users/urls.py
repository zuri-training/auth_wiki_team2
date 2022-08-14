from django.urls import re_path, include
from . import views

app_name = 'users'

urlpatterns = [
    re_path('profile', views.profile, name='profile'),
    re_path('update', views.update, name='update'),
]