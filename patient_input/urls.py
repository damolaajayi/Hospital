from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('patientinput/', views.home, name='patientinput'),
    path('doctorinfo/', views.doc, name='doctorinfo')
]