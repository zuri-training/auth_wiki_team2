from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    # UserPostListView,
    postpreference,
    # post_list
    )

from .import views

app_name = 'library'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('library/new/', PostCreateView.as_view(), name='post-create'),
    path('library/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-library'),
    path('library/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('library/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('library/<int:postid>/preference/<int:userpreference>', postpreference, name='postpreference'),

]
