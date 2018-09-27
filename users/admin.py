from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import DoctorSignUpForm, DoctorUserChangeForm
from .models import DoctorUser

class DoctorUserAdmin(UserAdmin):
	model = DoctorUser
	add_form = DoctorSignUpForm
	form = DoctorUserChangeForm


admin.site.register(DoctorUser, DoctorUserAdmin)