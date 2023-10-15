from django.contrib import admin
from django.urls import include, path

from . import views
import login.views

#Main Profile, Appointments List, Reports Summary, Edit Profile
urlpatterns = [
    path('', login.views.login, name='login'),
    path('patient-hub/', views.getPatient, name='patientHub'),
    path('specialist-hub/', views.getSpecialist, name='specialistHub'),
    path('patient-hub/edit/', views.editPatient, name='patientEdit'),
    path('specialist-hub/edit/', views.editSpecialist, name='specialistEdit'),
    path('', views.removeInvitedPatient, name='disconnectPatient'),
    # path('appointments/', views.patientAppointments, name='patientAppointments'),
    # path('appointments/', views.specialistAppointments, name='specialistAppointments'),
    # path('reports/', views.patientReports, name='patientReports'),
    # path('reports/', views.specialistReports, name='specialistReports'),
]