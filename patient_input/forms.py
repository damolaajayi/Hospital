from django import forms
from patients.models import patient
from .models import DoctorInfo

class PatientInput(forms.ModelForm):
	class Meta:
		model = patient
		fields = [
		'Reg_No',
		'first_name',
		'Last_name',
		'Email',
		'Patient_Age',
		'Gender',
		'Contact_No',
		'Patient_Address',
		]



class DoctorInformation(forms.ModelForm):
	class Meta:
		model = DoctorInfo
		fields = [
		'Name',  
		'Age', 
		'Contact_No', 
		'Gender', 
		'Department',
		]
