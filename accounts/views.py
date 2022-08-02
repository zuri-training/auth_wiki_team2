from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserAuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user
from .models import Profile, MyUser
import random
from django.core.mail import send_mail

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            otp = str(random.randint(1000, 9000))
            check_user = MyUser.objects.filter(email = email).first()
            check_profile = Profile.objects.filter(email = email).first()
            if check_user or check_profile:
                context = { 'message' : 'user already exists', 'class' : 'danger'}
                return render(request, 'accounts/signup.html', context)
            user = form.save() 
            email    = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            profile = Profile(user = user, otp = otp, email = email)
            profile.save()
            form.save()
            # send the user otp
            send_otp(email, otp)
            request.session['email'] = email
            return redirect('otp/')
        return render(request, 'accounts/signup.html', {'form':form})
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/signup.html')

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

def send_otp(email, otp):
    sub = '<p> Welcome to authwiki auth-wiki, we are thrilled to have you, to make sure your account is protected, please use the attached otp to verify your account. <p>Thank you</p></p>' + otp
    msg = 'Account verification'
    send_mail(
        subject= msg,
        message= "Otp Verification",
        from_email = "AuthWiki <email@gmail.com>",
        recipient_list = [email],
        html_message= sub
    )
    return None

def otp(request):
    email = request.session['email']
    context = {'email' : email}
    if request.method == "POST":
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(email = email).first()
        if otp == profile.otp:
            return redirect('/accounts/login')
        else:
            print('oops')
            message = { 'message' : 'wrong otp', 'class' : 'danger', 'email': email}
            return render(request, 'accounts/otp.html')

    return render(request, 'accounts/otp.html', context)