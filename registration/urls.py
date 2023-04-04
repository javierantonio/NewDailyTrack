from django.contrib import admin
from django.urls import include, path

import landingPage.views
from . import views

urlpatterns = [
    path('patient/', views.patientRegistration, name='patientRegistration'),
    path('specialist/', views.specialistRegistration, name='specialistRegistration'),
    path('', landingPage.views.home, name='landing-page'),

]
