from django.views.generic import TemplateView
from django.shortcuts import render

def index(request):
    return render(request, 'hospital/home.html')

class HomePageView(TemplateView):
	template_name = 'home.html'
