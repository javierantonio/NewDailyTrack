from django.shortcuts import render
from . import patientRegistrationForm


# Create your views here.

def home(request):
    return render(request, 'registration.html')


def patientRegistration(request):
    if request.method == 'POST':
        if patientRegistrationForm.processPatientRegistration(request):
            return render(request, 'registration.html')

    else:
        return render(request, 'registration.html')


def specialistRegistration(request):
    if request.method == 'POST':
        return None
        # if specialistRegistrationForm.processSpecialistRegistration(request):
        #     return render(request, 'registration.html')

    else:
        return render(request, 'specialistRegistration.html')
