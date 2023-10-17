from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import sqlite3

from . import specialistRegistrationForm, patientRegistrationForm

# Create your views here.

def home(request):
    return render(request, 'userSelect.html')


def patientRegistration(request):
    if request.method == 'POST':
        if patientRegistrationForm.processPatientRegistration(request)==True:
            return redirect(reverse('login'))
        else:
            return render(request, 'patientRegistration.html', {'error_message': 'There is already an account tied to this email. You could use another email or log in using the correct credentials of the email you just entered.', 'error_header':'📧 User already exists!'})
    return render(request, 'patientRegistration.html')


def specialistRegistration(request):
    if request.method == 'POST':
        if specialistRegistrationForm.processSpecialistRegistration(request)==True:
            return redirect(reverse('login'))
        else:
            return render(request, 'specialistRegistration.html', {'error_message': 'There is already an account tied to this email. You could use another email or log in using the correct credentials of the email you just entered.', 'error_header':'📧 User already exists!'})
    else:
        return render(request, 'specialistRegistration.html')