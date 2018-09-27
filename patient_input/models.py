from django.db import models
from patients.models import patient
# Create your models here.
class DoctorInfo(models.Model):
	SEX = (
		('M', 'Male'),
		('F', 'Female'),
		)
	Name       = models.CharField(max_length=100)
	ID         = models.IntegerField(primary_key=True)
	Age        = models.CharField(max_length=50)
	Contact_No = models.IntegerField()
	Room       = models.IntegerField()
	Gender     = models.CharField(max_length=1, choices=SEX)
	Department = models.CharField(max_length=100)

