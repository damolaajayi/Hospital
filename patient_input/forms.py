from django import forms
from patients.models import patient

class PatientInput(forms.Form):
	Reg_No = 			forms.IntegerField()
	first_name	= 		forms.CharField(max_length=100)
	Last_name	=		forms.CharField(max_length=100)
	Email = 	        forms.EmailField(max_length=100)
	Patient_Age = 		forms.CharField(max_length=30)
	Gender = 			forms.CharField(max_length=30)
	Patient_Address = 	forms.CharField(max_length=250)
	Contact_No = 		forms.IntegerField()
	Room_No = 			forms.IntegerField()


class DoctorInformation(forms.Form):
	Name  = forms.CharField()
	Age   = forms.CharField()
	Contact_No = forms.CharField()
	Room = forms.CharField()
	Gender = forms.CharField()
	Department = forms.CharField()


def clean(self):
	cleaned_data = super(PatientInput, self)
	Reg_No = cleaned_data.get('Reg No')
	first_Name = cleaned_data.get('first_Name')
	Last_Name = cleaned_data.get('Last Name')
	Email = cleaned_data.get('Email')
	Patient_Age = cleaned_data.get('Patient Age')
	Gender = cleaned_data.get('Gender')
	Patient_Address = cleaned_data.get('Patient	Address')
	Contact_No = cleaned_data.get('Contact')
	Room = cleaned_data.get('Room')
	date = cleaned_data.get('Date')