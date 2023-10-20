from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('home', views.dashboardLanding, name='patientDashboardHome'),
    path('notes/', include('consultationNotes.urls')),
    path('emoticards/', include('steppingStones.urls')),
    path('journals/', include('journal.urls')),
    path('viewProfile/<str:userId>/', views.viewProfile, name='viewProfile'),
    # path('', include('profileHub.urls')),
    # path('', include('consultationNotes.urls')),
]
