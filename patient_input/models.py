from django.db import models
from patients.models import patient
# Create your models here.
class DoctorInfo(models.Model):
	SEX = (
		('M', 'Male'),
		('F', 'Female'),
		)
	Name       = models.CharField(max_length=100, primary_key=True)
	Age        = models.CharField(max_length=50)
	Contact_No = models.BigIntegerField()
	Gender     = models.CharField(max_length=6, choices=SEX)
	Department = models.CharField(max_length=100)

	def __str__(self):
		return self.Name
