from django.contrib import admin
from library.models import Post, Comment, Preference, category


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Preference)
admin.site.register(category)