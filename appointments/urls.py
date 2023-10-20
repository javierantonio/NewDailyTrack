from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.calendarView, name='appointmentPage'),
    path('calendar/', views.calendarView, name='appointmentCalendar'),
]
