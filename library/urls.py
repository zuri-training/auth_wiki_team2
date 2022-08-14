from django.urls import path
from .views import (
    LibraryView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    postpreference,
    )

from .import views

app_name = 'library'

urlpatterns = [
<<<<<<< HEAD
    path('', CategoryListView.as_view(), name='home'),
    path('post_list', PostListView.as_view(), name='post_list'),
=======
    path('', LibraryView.as_view(), name='home'),
    path('category/<str:name>', PostListView.as_view(), name='library-category'),
>>>>>>> 872627bd4bf8a95a75a48198aedf16a55caefc1d
    path('library/new/', PostCreateView.as_view(), name='post-create'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('library/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('library/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('library/<int:postid>/preference/<int:userpreference>', postpreference, name='postpreference'),

]
