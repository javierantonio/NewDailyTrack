from django.contrib import admin
from django.urls import include, path

from . import views

# Journal, Appointments, Specialist, Emoticards, Timely Reports, Profile
urlpatterns = [
    path('', views.landing, name='landing'),
    path('', include('journal.urls')),
    path('', include('steppingStones.urls')),
    path('', include('patientDirectory.urls')),
    path('', include('profileHub.urls')),
    path('', include('consultationNotes.urls')),
    path('specialist/', include('patientDashboard.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    # path('', include('summaries.urls')),
]
