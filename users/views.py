from django.urls import reverse_lazy
from django.views import generic


from .forms import DoctorSignUpForm

class SignUp(generic.CreateView):
	form_class = DoctorSignUpForm
	success_url = reverse_lazy('users:login')
	template_name = 'signup.html' 
	