from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.specialistCalendarView, name='appointmentPage'),
    path('calendar/', views.specialistCalendarView, name='appointmentCalendar'),
    path('create/', views.createAppointment, name='appointmentCreate'),
    path('history/', views.appointmentHistory, name='appointmentHistory'),
    path('calendar/ca/', views.confirmAppointment, name='appointmentConfirm'),
    path('calendar/da/', views.declineAppointment, name='appointmentDecline'),
    path('calendar/ca/', views.rescheduleAppointment, name='appointmentResched'),
]
