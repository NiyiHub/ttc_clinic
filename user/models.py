from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.utils.timezone import now


class UserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password=None):
		if not email:
			raise ValueError('Email must be provided.')
		if not first_name:
			raise ValueError('First name must be provided.')
		if not last_name:
			raise ValueError('Last name must be provided.')

		email = self.normalize_email(email)
		email = email.lower()

		user = self.model(
				email=email,
				first_name=first_name,
				last_name=last_name
		)

		user.set_password(password)
		user.save(using=self._db)

		return user 

	def create_doctor(self, email, first_name, last_name, password=None):
		user = self.create_user(email, first_name, last_name, password)

		user.is_doctor = True
		user.save(using=self._db)

		return user

	def create_superuser(self, email, first_name, last_name, password=None):
		user = self.create_user(email, first_name, last_name, password)

		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)

		return user

class TtcUser(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	email = models.EmailField(max_length=60, unique=True)
	phone = models.CharField(max_length=14)
	image = models.ImageField(upload_to='Images/', null=True, blank=True)
	date_joined = models.DateTimeField(default=now)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	is_doctor = models.BooleanField(default=False)
	
	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', ]

	def __str__(self):
		return self.email