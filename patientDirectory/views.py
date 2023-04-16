from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from pipenv.patched.safety.alerts import alert

from journal import journalControllers
from patientDirectory.models import Enrollment, PatientList
from registration.models import Profile


# Create your views here.

@login_required
def unconfirmedList(request):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Specialist":
            if request.method == "GET":
                return render(request, 'unconfirmedPatients.html')
        else:
            return redirect('landing')
    else:
        return redirect('landing')

def confirmedList(request):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Specialist":
            if request.method == "GET":
                return render(request, 'confirmedPatients.html')
        else:
            return redirect('landing')
    else:
        return redirect('landing')
