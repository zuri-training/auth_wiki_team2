from django.http import HttpResponse
from django.shortcuts import render
from authwiki_app.models import Library

# Create your views here.
def index(request):
    return render(request, 'authwiki_app/homepage.html')

def service(request):
    return render(request, 'authwiki_app/service.html')     


def library(request):
    auth_library = Library.objects.all()
    context = {'auth_library':auth_library}
    return render(request, 'authwiki_app/library.html', context)

def Faq(request):
    return render(request, 'authwiki_app/faq.html')

def blog(request):
    return render(request, 'authwiki_app/blog.html')
