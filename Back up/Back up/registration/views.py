from django.http import HttpResponse
from django.shortcuts import render

from .models import Patient, PatientList, Specialist, User


def home(request):
    return HttpResponse('Registration Homepage')
