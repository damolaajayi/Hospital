from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('patientsview/', views.patient_list, name='patient_list'),
    path('doctor/', views.doct, name='doct'),
    path('doctorview/', views.docview, name='docview'),
    path('prescription/', views.prescrip, name='prescrip'),
    path('patient/', views.singlepatient, name='singlepatient'),

]