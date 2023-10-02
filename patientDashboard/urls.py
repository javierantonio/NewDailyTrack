from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.dashboardLanding, name='patientDashboardHome'),
    # path('', include('journal.urls')),
    # path('', include('steppingStones.urls')),
    # path('', include('patientDirectory.urls')),
    # path('', include('profileHub.urls')),
    # path('', include('consultationNotes.urls')),
]
