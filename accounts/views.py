from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()      
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
