from django.contrib import admin
from django.urls import include, path

from . import views
from summaryReports import views as summary

# Journal, Appointments, Specialist, Emoticards, Timely Reports, Profile
urlpatterns = [
    path('', views.landing, name='landing'),
    path('', include('journal.urls')),
    path('', include('steppingStones.urls')),
    path('', include('patientDirectory.urls')),
    path('', include('profileHub.urls')),
    path('', include('consultationNotes.urls')),
    path('specialist/', include('patientDashboard.urls')),    
    path('summaries/', summary.summaries, name='summaries'),
    # path('', include('summaries.urls')),
]
