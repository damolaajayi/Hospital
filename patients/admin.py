from django.contrib import admin
from .models import patient, Prescription

# Register your models here.
admin.site.register(patient)
admin.site.register(Prescription)
