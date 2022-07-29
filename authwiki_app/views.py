from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import otp

# Create your views here.
def verify_otp(request):
    if request.method == "POST":
        Otp = int(request.POST.get('subject'))
        user = int(request.POST.get('message'))
        retrieve = otp.objects.get(hashed = Otp)
        user = otp.objects.get( user = user)
        print(retrieve)
        return HttpResponse('processed')
    return render(request, 'form.html')

def send_otp(request):
    if request.method == "POST":
        sub = '<p> Welcome to authwiki authentication library, we are thrilled to have you, to make sure your account is protected, please use the attached otp to verify your account,otp <b>1010</b>. <p>Thank you</p></p>'
        msg = 'Account verification'
        email = request.POST.get('email')
        otp.userId = "123456"
        otp.otp = "1234"
        otp.date = "12/12/2020"
        Otp = otp( hashed = 4567,)
        Otp.save()
        send_mail(
            subject= msg,
            message= "Otp Verification",
            from_email = "AuthWiki <olatundesuccess54@gmail.com>",
            recipient_list = [email],
            html_message= sub
        )
        return HttpResponse("email send that !")
    return render(request, 'form.html')