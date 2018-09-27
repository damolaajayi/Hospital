from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DoctorUser

class DoctorSignUpForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = DoctorUser
		fields = ('username', 'email')

class DoctorUserChangeForm(UserChangeForm):

	class Meta:
		model = DoctorUser
		fields = UserChangeForm.Meta.fields