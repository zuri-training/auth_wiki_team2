from django.http import HttpResponse
from django.shortcuts import render, redirect
from authwiki_app.forms import Contactforms
from django.contrib import messages
# from authwiki_app.models import Library

# Create your views here.
def index(request):
    return render(request, 'authwiki_app/homepage.html')

def service(request):
    return render(request, 'authwiki_app/service.html')     


def Faq(request):
    return render(request, 'authwiki_app/faq.html')

def blog(request):
    return render(request, 'authwiki_app/blog.html')

def library(request):
    return render(request, 'authwiki_app/library.html')

def about(request):
    return render(request, 'authwiki_app/about.html')

def contact(request):
    if request.method == 'POST':
        contact = Contactforms(request.POST)
        if contact.is_valid():
            contact.save()
            messages.info(request, 'Message saved successfully')
        return render(request, 'authwiki_app/contact_us.html')
    else:
        return render(request, 'authwiki_app/contact_us.html')


def doc(request):
    return render(request, 'authwiki_app/doc.html')

def text(request):
    return render(request, 'authwiki_app/text.html')
