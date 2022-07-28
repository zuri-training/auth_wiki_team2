from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.

#manager for our model
class MyUserManager(BaseUserManager):
	def create_user(self, email, username, firstname, lastname, password=None):
		# for creating a user 
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a Username')

		user = self.model(
				email = self.normalize_email(email), 
				username=username,
				firstname=firstname,
				lastname=lastname,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, firstname, lastname, password):
		user = self.create_user(
				email=self.normalize_email(email),
				password=password,
				username=username,
				firstname=firstname,
				lastname=lastname,
			)
		user.is_admin = True
		user.is_staff=True
		user.is_superuser=True
		user.save(using=self._db)
		return user

#our model
class User(AbstractBaseUser):
	email = models.EmailField(verbose_name='email address', max_length=60, unique=True,)
	username = models.CharField(verbose_name='username', max_length=30, unique=True)
	firstname = models.CharField(verbose_name='firstname', max_length=30, default=0000)
	lastname = models.CharField(verbose_name='lastname', max_length=30, default=0000)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, authwiki_app):
		return True

