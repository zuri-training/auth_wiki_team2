from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('blog/create/', views.blog_create, name='create'),
    path('blog/<str:slug>/detail', views.blogs_detail, name="detail"),
]
