from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Profile
import random

# Create your views here.
def index(request):
    return render(request, 'authwiki_app/index.html')

def service(request):
    return render(request, 'authwiki_app/service.html')

def send_otp(email, otp):
    sub = '<p> Welcome to authwiki authentication library, we are thrilled to have you, to make sure your account is protected, please use the attached otp to verify your account. <p>Thank you</p></p>' + otp
    msg = 'Account verification'
    send_mail(
        subject= msg,
        message= "Otp Verification",
        from_email = "AuthWiki <email@gmail.com>",
        recipient_list = [email],
        html_message= sub
    )
    return None

def register(request):
    if request.method == "POST":
        otp = str(random.randint(1000, 9000))
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        check_user = User.objects.filter(email = email).first()
        check_profile = Profile.objects.filter(email = email).first()
        if check_user or check_profile:
            context = { 'message' : 'user already exists', 'class' : 'danger'}
            return render(request, 'form.html', context)
        user = User(email = email, username = name, password = password)
        user.save()
        profile = Profile(user = user, otp = otp, email = email)
        profile.save()
        send_otp(email, otp)
        request.session['email'] = email
        return redirect('otp')
    return render(request, 'form.html')

def otp(request):
    email = request.session['email']
    context = {'email' : email}
    if request.method == "POST":
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(email = email).first()

        if otp == profile.otp:
            return HttpResponse("account verified")
        else:
            context = { 'message' : 'wrong otp', 'class' : 'danger', 'email': email}
            return render(request, 'otp.html', context)

    return render(request, 'otp.html', context)