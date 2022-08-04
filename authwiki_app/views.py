from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'authwiki_app/index.html')

def service(request):
    return render(request, 'authwiki_app/service.html')

def social_proof(request):
    return render(request, 'authwiki_app/social_proof.html')

