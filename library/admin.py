from django.contrib import admin
from library.models import Post, Comment, Preference, PostCategory


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Preference)
admin.site.register(PostCategory)