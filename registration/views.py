from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import specialistRegistrationForm, patientRegistrationForm


# Create your views here.

def home(request):
    return render(request, 'registration.html')


def patientRegistration(request):
    if request.method == 'POST':
        if patientRegistrationForm.processPatientRegistration(request):
            return redirect('login')

    else:
        return render(request, 'landing-page')


def specialistRegistration(request):
    if request.method == 'POST':
        if specialistRegistrationForm.processSpecialistRegistration(request):
            return render(request, '')

    else:
        return render(request, 'specialistRegistration.html')
