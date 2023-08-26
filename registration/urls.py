from django.contrib import admin
from django.urls import include, path

import home.views
from . import views
import login.views

urlpatterns = [
    path('patient/', views.patientRegistration, name='patientRegistration'),
    path('specialist/', views.specialistRegistration, name='specialistRegistration'),
    path('', views.home, name='registrationSelection'),
    path('accounts/', include('allauth.urls')),
    path('login/', login.views.login, name='loginPage'),
    # path('', login.views.home, name='google')
    

]
