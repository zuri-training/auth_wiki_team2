
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserAuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Profile, MyUser
import random, time
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            otp = str(random.randint(1000, 9000))
            check_user = MyUser.objects.filter(email = email).first()
            check_profile = Profile.objects.filter(email = email).first()
            if check_user or check_profile:
                 messages.error(request, 'user already exist')
                 return HttpResponseRedirect(request.path_info)
            user = form.save() 
            email    = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            profile = Profile(user = user, otp = otp, email = email)
            profile.save()
            form.save()
            # send the user otp
            send_otp(email, otp)
            request.session['email'] = email
            request.session['password'] = password
            return redirect('otp/')
        return render(request, 'accounts/signup.html')
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/signup.html')

def logout_view(request):
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
        check_profile = MyUser.objects.filter(otp_check = False).first()
        if check_profile:
            messages.error(request, 'account not verified')
            return HttpResponseRedirect(request.path_info)
        if user:
            login(request, user)
            return redirect('/')
        messages.info(request, 'Invalid information. please try again')        
        return render(request, 'accounts/sign_in.html')
    else:
        form = UserAuthenticationForm()
        return render(request, 'accounts/sign_in.html')

def send_otp(email, otp):
    sub = '<p> Welcome to authwiki, we are thrilled to have you, to make sure your account is protected, please use the attached otp to verify your account. <p>Thank you</p></p>' + otp
    msg = 'Account verification'
    send_mail(
        subject= msg,
        message= "Otp Verification",
        from_email = "AuthWiki <authwiki29@gmail.com>",
        recipient_list = [email],
        html_message= sub
    )
    return None

def otp(request):
    email = request.session['email']
    password = request.session['password']
    user =  authenticate(email=email, password=password)
    if request.method == "POST":
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(email = email).first()
        if profile:        
            if otp == profile.otp:
                MyUser.objects.update(otp_check = True)
                Profile.objects.filter(email = email).delete()
                login(request, user)
                return redirect('/')
            else:
                 messages.error(request, 'incorrect otp')
                 return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'otp not found, try requesting again')
            return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/otp.html')