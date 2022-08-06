from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

def is_users(profile_user, logged_user):
    return profile_user == logged_user

# Create your views here.
@login_required
def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update.html', context)

