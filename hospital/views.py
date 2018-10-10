from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import DoctorSignUpForm


class HomePageView(TemplateView):
	template_name = 'home.html'

class SignUp(generic.CreateView):
	form_class = DoctorSignUpForm
	success_url = reverse_lazy('hospital:login')
	template_name = 'signup.html'