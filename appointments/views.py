from django.shortcuts import render
# from flask import jsonify
from .models import Appointments, DeclinedAppointments, AcceptedAppointments, RescheduledAppointments


def getAppointments(specialistId):
    appointments = Appointments.objects.filter(specialist = specialistId)

