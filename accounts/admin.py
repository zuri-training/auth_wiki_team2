from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm, UserAuthenticationForm, UserUpdateForm
from .models import User

# Register your models here.

class UserAdmin(UserAdmin):
	form = UserUpdateForm
	add_form = UserRegistrationForm

	# define fields to be used in displaying the User model.

	list_display = ('email', 'first_name', 'last_name','is_admin')
	list_filter = ('email', 'first_name', 'last_name','is_admin')
	fieldsets = (
	   (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
	   ('Permissions', {'fields': ('is_admin',)}),
	)
	add_fieldsets = (
	   (None, {
	       'classes': ('wide',),
	       'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
	   }),
	)
	ordering = ('email',)
	filter_horizontal = ()

 
#I'm registering the new UserAdmin
admin.site.register(User, UserAdmin)
 