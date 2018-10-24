from django import forms
from .models import Prescription, patient


class DoctorForm(forms.ModelForm):
	class Meta:
		model = Prescription
		fields = [
				'patient',
				'Complaint',
				'Prescription',
				'Remarks',
				]





#class DoctorForm(forms.Form):
	#patient = forms.ModelChoiceField(queryset=patient.objects.all())
	#Complaint = forms.CharField(widget=forms.Textarea)
	#Prescription = forms.CharField(widget=forms.Textarea)
	#Remarks = forms.CharField(widget=forms.Textarea)
	#Date = forms.DateField()
