from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
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
    return render(request, 'patientDashboard.html', context={'data': getPatients(request.user)})

def getPatients(userData):
    specialistId = Specialist.objects.get(profile = Profile.objects.get(user=userData))
    patients = PatientList.objects.filter(specialist = specialistId, patientListStatus = 'A').order_by('created_at')
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

def getLatestEmoticard(patientID):
    # steppingStonesData = SteppingStone.objects.filter(patient = get_object_or_404(Patient, profile_id=patientID)).order_by('-created_at').first()
    steppingStonesData = SteppingStone.objects.filter(patient = get_object_or_404(Patient, profile_id=patientID))
    if steppingStonesData is not None:
        if steppingStonesData.exists():
            print(steppingStonesData.order_by('-created_at').first().created_at)
            return moodText(steppingStonesData.order_by('-created_at').first().moodLevel)
        else:
            return "No Entry"
    else:
        return "No Entry"

def getUserProfile(request):
    patientId = request.GET.get('patientIndex')
    for user in data:
        if user['id'] == patientId:
            user_data = user
            break
    return JsonResponse(user_data)

def moodText(mood):
    if mood == 5:
        return 'Terrible'
    elif mood == 4:
        return 'Bad'
    elif mood == 3:
        return 'Okay'
    elif mood == 2:
        return 'Good'
    elif mood == 1:
        return 'Awesome'
