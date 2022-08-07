from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils import timezone
from accounts.models import MyUser

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('date')
    return render(request,'blog/blog_list.html', {'blogs':blogs})

def blogs_detail(request, slug):
    blogs = Blog.objects.get(slug=slug)
    print(blogs)
    return render(request, 'blog/blog_detail.html', {'blogs':blogs})

@login_required(login_url='/accounts/login')
def blog_create(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            # save blog to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:list')
    else:
        form = forms.CreateBlog()
    return render(request, 'blog/blog_create.html', {'form':form})