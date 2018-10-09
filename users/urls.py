from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('users/', include('django.contrib.auth.urls')),
]
