from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url('profile', views.profile, name='profile'),
    url('update', views.update, name='update'),
]