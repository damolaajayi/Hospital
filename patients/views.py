from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import patient, Prescription
from .forms import DoctorForm
from patient_input.models import DoctorInfo
from django.db.models import Q

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/users/login")
def patient_list(request):
	queryset = patient.objects.order_by('-Reg_No')
	query = patient.objects.all()
	qs = request.GET.get("q")
	if qs:
		query = query.filter(
			Q(first_name__icontains=qs)|
			Q(Last_name__icontains=qs)|
			Q(Reg_No__icontains=qs)
			).distinct()
	context = {
		"patient": queryset,
		"patient": query
	}
	return render(request, 'patients/patients.html', context)

@login_required(login_url="/users/login")
def doct(request):
	form = DoctorForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=True)
	context = {
			'form': form
	}
	return render(request, 'patients/ex.html', context)


@login_required(login_url="/users/login")
def docview(request):
	query = DoctorInfo.objects.all()
	qs = request.GET.get("q")
	if qs:
		query = query.filter(
			Q(Name__icontains=qs)|
			Q(ID__icontains=qs)|
			Q(Age__icontains=qs)
			).distinct()

	context = {
		"doctor": query
	}
	return render(request, 'patients/dove.html', context)


@login_required(login_url="/users/login")
def prescrip(request):
	qs = Prescription.objects.all().select_related()
	q = patient.objects.all().select_related()
	context = {
	"qs": qs,
	'q': q,
	}
	return render(request, 'patients/prescription.html', context)


@login_required(login_url="/users/login")
def singlepatient(request):
	q = patient.objects.all()
	query = Prescription.objects.all()
	context = {
	"patient" : q,
	"Prescription": query
	}
	return render(request, 'patients/single.html', context)


