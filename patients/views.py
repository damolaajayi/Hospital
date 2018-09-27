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

	#search_term = ''
	#if 'search' in request.GET:
	#	search_term = request.GET['search']
	#	query = query.filter(patient__icontains=search_term) | filter(first_name__icontains=search_term)
	context = {
		"patient": queryset,
		"patient": query
	}
	return render(request, 'patients/patients.html', context)

@login_required(login_url="/users/login")
def doct(request):
	if request.method == 'POST':
		form = DoctorForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			Prescription.objects.create(**form.cleaned_data)
	else:
		form = DoctorForm()
	context = {
			'form': form
	}
	return render(request, 'patients/ex.html', context)


@login_required(login_url="/users/login")
def docview(request):
	query = DoctorInfo.objects.all()
	search_term = ''
	if 'search' in request.GET:
		search_term = request.GET['search']
		query = query.filter(ID__icontains=search_term, Name__exact=search_term)

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
	context = {
	"patient" : q
	}
	return render(request, 'patients/single.html', context)


