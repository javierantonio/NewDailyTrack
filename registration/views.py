from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import specialistRegistrationForm, patientRegistrationForm


# Create your views here.

def home(request):
    return render(request, 'userSelect.html')


def patientRegistration(request):
    if request.method == 'POST':
        if patientRegistrationForm.processPatientRegistration(request):
            return redirect(reverse('login'))
    return render(request, 'patientRegistration.html')


def specialistRegistration(request):
    if request.method == 'POST':
        if specialistRegistrationForm.processSpecialistRegistration(request):
            return redirect(reverse('login'))
    else:
        return render(request, 'specialistRegistration.html')
