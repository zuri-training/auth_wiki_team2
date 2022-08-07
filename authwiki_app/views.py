from django.http import HttpResponse
from django.shortcuts import render
# from authwiki_app.models import Library

# Create your views here.
def index(request):
    return render(request, 'authwiki_app/homepage.html')

def service(request):
    return render(request, 'authwiki_app/service.html')     


def Faq(request):
    return render(request, 'authwiki_app/faq.html')
