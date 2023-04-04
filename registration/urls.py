from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('patient/', views.patientRegistration, name='patientRegistration'),
    path('specialist/', views.specialistRegistration, name='specialistRegistration'),

]
