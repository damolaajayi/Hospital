from django.contrib.auth.models import AbstractUser, UserManager

class DoctorUserManager(UserManager):
	pass


class DoctorUser(AbstractUser):
	objects = DoctorUserManager()