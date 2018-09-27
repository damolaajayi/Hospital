from django.shortcuts import render
from .forms import PatientInput, DoctorInformation
from patients.models import patient
from .models import DoctorInfo
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login")
def home(request):
	if request.method == 'POST':
		form = PatientInput(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			patient.objects.create(**form.cleaned_data)
	else:
		form = PatientInput()
	return render(request, 'patient_input/home.html', {'form': form})


@login_required(login_url="/users/login")
def doc(request):
	if request.method == 'POST':
		form = DoctorInformation(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			DoctorInfo.objects.create(**form.cleaned_data)
	else:
		form = DoctorInformation()
	return render(request, 'patient_input/doc.html', {'form': form})
