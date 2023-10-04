from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from patientDirectory.models import PatientList
from registration.models import Specialist, Profile, Patient
from steppingStones.models import SteppingStone

def dashboardLanding(request):
    # return HttpResponse('naur')
    # specialistId = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    # patients = PatientList.objects.filter(specialist = specialistId)
    
    # # print(patients[0])
    # for element in patients:
    #     print(element.patient)
    print(request)
    return render(request, 'patientDashboard.html', context={'data': getPatients(request.user)})

def getPatients(userData):
    specialistId = Specialist.objects.get(profile = Profile.objects.get(user=userData))
    patients = PatientList.objects.filter(specialist = specialistId)
    patientArray = {}
    index = 0
    for element in patients:
        patientDetails = Profile.objects.get(email = element.patient)
        patientArray[index] = {
            'id': patientDetails.profileID,
            'patientName': patientDetails.user.first_name+' '+patientDetails.user.last_name,
            'latestMood': getLatestEmoticard(patientDetails.profileID)
        }
        # patientArray.update({
        #     'patient{index}' : patientDetails.profileID
        # })
        index+=1

    return patientArray

def getLatestEmoticard(patientEmail):
    return ''
    steppingStonesData = str(SteppingStone.objects.order_by('-created_at').get(patient = patientEmail)).split(' ')
    print(steppingStonesData)    
    return steppingStonesData

def getUserProfile(request):
    patientId = request.GET.get('patientIndex')
    for user in data:
        if user['id'] == patientId:
            user_data = user
            break
    return JsonResponse(user_data)
