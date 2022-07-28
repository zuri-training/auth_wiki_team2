from django import forms
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(UserCreationForm):
    #form for new user registration
    email = forms.EmailField(max_length=60, help_text = 'Required. Add a valid email address')
    username = forms.CharField(max_length=30, help_text = 'Input your Username')
    firstname = forms.CharField(max_length=30, help_text = 'Input your Firstname')
    lastname = forms.CharField(max_length=30, help_text = 'Input your Lastname')

    class Meta:
        model = User
        fields = ('email', 'username', 'firstname', 'lastname', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['username'],self.fields['firstname'],self.fields['lastname'],self.fields['password1'],self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        #verifying that the email hasn't been previously registered
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already in use")
        return email

    def clean_password2(self):
       # Check that the two password entries match
       password1 = self.cleaned_data.get("password1")
       password2 = self.cleaned_data.get("password2")
       if password1 and password2 and password1 != password2:
           raise ValidationError("Passwords don't match")
       return password2


class UserAuthenticationForm(forms.ModelForm):
    # form for when user logs in
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  User
        fields =  ('email', 'password')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):

        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        #verifying your login details
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class UserUpdateForm(forms.ModelForm):
    #form for updating User Info
    class Meta:
        model  = User
        fields = ('email', 'password', 'username', 'firstname', 'lastname')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
                   'username':forms.TextInput(attrs={'class':'form-control'}),
                   'firstname':forms.TextInput(attrs={'class':'form-control'}),
                   'lastname':forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):

        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password'],self.fields['username'],self.fields['firstname'],self.fields['lastname']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk = self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError("Email is already in use")

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                user = User.objects.exclude(pk = self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError("Username is already in use")





# class UserCreationForm(forms.ModelForm):
#     email = forms.EmailField(max_length=60, help_text = 'Required. Add a valid email address')
#     username = forms.CharField(max_length=30, help_text = 'Input your Username')
#     firstname = forms.CharField(max_length=30, help_text = 'Input your Firstname')
#     lastname = forms.CharField(max_length=30, help_text = 'Input your Lastname')
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     # class Meta:
#     #     model = User
    #     fields = ('email', 'username', 'firstname', 'lastname', 'password1', 'password2')


    # def clean_email(self):
    #     #verifying that the email hasn't been previously registered
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("Email is already in use")
    #         return email

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Passwords don't match")
    #         return password2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #         return user

