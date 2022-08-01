from pickle import FALSE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Email is required")
		if not username:
			raise ValueError("Username is required")

		user = self.model(
			email = self.normalize_email(email),
			username = username
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password=None):
		user = self.create_user(
			email = self.normalize_email(email),
			username = username,
		)
		user.is_admin = True
		user.is_superuser = True
		user.is_staff = True
		user.set_password(password)
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	username = models.CharField(verbose_name="username", max_length=100, unique=True)
	email = models.EmailField(verbose_name="email ", max_length=60, unique=True)
	date_joined = models.DateTimeField(verbose_name = "date_joined", auto_now_add=True)
	last_login = models.DateTimeField(verbose_name="last_login", auto_now_add=True)
	is_admin = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['username']

	objects = MyUserManager()

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
