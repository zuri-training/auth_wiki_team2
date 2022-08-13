from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from accounts.models import MyUser
from django.urls import reverse


class Post(models.Model):
    title = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    code_snippet = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('PostCategory', on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    downloadnumber = models.IntegerField(default=0)
    github = models.URLField(max_length=500, null=True, blank=True,)
    download = models.URLField(max_length=500, null=True, blank=True,)
    images = models.ImageField(upload_to='library_images', blank=True)

    
    def __str__(self):
        return self.title

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()


class PostCategory(models.Model):
    name = models.CharField(verbose_name='name', max_length=150, default="Name")
    images = models.ImageField(upload_to='library_images', blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_connected.title


class Preference(models.Model):
    user= models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")


