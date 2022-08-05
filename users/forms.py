from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from accounts.models import MyUser


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = MyUser

        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name','middle_name','last_name','position','image','cover','bio','city','country','website','facebook','twitter','instagram','github']
