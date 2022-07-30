from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserAuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            email    = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password = raw_pass)     
            # log the user in
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/')
    if request.method  == 'POST':
        form = UserAuthenticationForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('/')
    else:
        form = UserAuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})