from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import RegistrationForm, UserAuthenticationForm, UserUpdateForm
from .models import User
from django.contrib.auth import get_user_model

# Register your models here.
 
User = get_user_model()

class UserAdmin(UserAdmin):
	form = UserUpdateForm
	add_form = RegistrationForm

	# define fields to be used in displaying the User model.

	list_display = ('email', 'username', 'firstname', 'lastname','is_admin')
	list_filter = ('email', 'username', 'firstname', 'lastname','is_admin')
	fieldsets = (
	   (None, {'fields': ('email', 'username', 'firstname', 'lastname', 'password')}),
	   ('Permissions', {'fields': ('is_admin',)}),
	)
	add_fieldsets = (
	   (None, {
	       'classes': ('wide',),
	       'fields': ('email', 'username', 'firstname', 'lastname', 'password1', 'password2'),
	   }),
	)
	ordering = ('email',)
	filter_horizontal = ()

 
#I'm registering the new UserAdmin
admin.site.register(User, UserAdmin)
 