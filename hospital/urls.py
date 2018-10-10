from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'hospital'
urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='hospital/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='hospital/logout.html'), name="logout"),
    ]