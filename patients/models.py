from django.db import models
import datetime





class patient(models.Model):
	SEX = (
		('M', 'Male'),
		('F', 'Female'),
		)
	
	Reg_No          = models.SmallIntegerField(primary_key=True)
	first_name      = models.CharField(max_length=25)
	Last_name       = models.CharField(max_length=25)
	Email           = models.EmailField(max_length=50)
	Patient_Age     = models.CharField(max_length=10)
	Gender          = models.CharField(max_length=6, choices=SEX)
	Patient_Address = models.TextField(max_length=200)
	Contact_No      = models.IntegerField()
	Room_No         = models.IntegerField()
	time 			= models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s %s" % (self.first_name, self.Last_name)





	

class Prescription(models.Model):
	patient         = models.ForeignKey(patient, on_delete=models.CASCADE)
	Complaint       = models.TextField(max_length=300)
	Prescription    = models.TextField(max_length=200)
	Remarks         = models.TextField(max_length=200)
	Date            = models.DateTimeField('Date prescribed')

	def __str__(self):
		return self.Prescription

	class Meta:
		ordering = ('patient',)

