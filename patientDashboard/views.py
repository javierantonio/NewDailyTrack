from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from patientDirectory.models import PatientList
from registration.models import Specialist, Profile, Patient

def dashboardLanding(request):
    # return HttpResponse('naur')
    # specialistId = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    # patients = PatientList.objects.filter(specialist = specialistId)
    
    # # print(patients[0])
    # for element in patients:
    #     print(element.patient)
    return render(request, 'patientDashboard.html', context={'data': getPatients(request.user)})

def getPatients(userData):
    specialistId = Specialist.objects.get(profile = Profile.objects.get(user=userData))
    patients = PatientList.objects.filter(specialist = specialistId)
    patientArray = {}
    index = 0
    for element in patients:
        patientDetails = Profile.objects.get(email = element.patient)
        patientArray[index] = patientDetails.profileID
        # patientArray.update({
        #     'patient{index}' : patientDetails.profileID
        # })
        index+=1

    print(patientArray[0])
    return patientArray
