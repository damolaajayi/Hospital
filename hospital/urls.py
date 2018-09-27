from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
    path('home', views.index, name='index'),
    ]