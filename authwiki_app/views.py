from django.http import HttpResponse
from django.shortcuts import render
from authwiki_app.models import Library

# Create your views here.
def index(request):
    return render(request, 'authwiki_app/index.html')

def service(request):
    return render(request, 'authwiki_app/service.html')     

def social_proof(request):
    return render(request, 'authwiki_app/social_proof.html')

def library(request):
    auth_library = Library.objects.all()
    context = {'auth_library':auth_library}
    return render(request, 'authwiki_app/library.html', context)

def Faq(request):
    return render(request, 'authwiki_app/faq.html')
