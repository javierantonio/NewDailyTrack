from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
#Import Models
from registration.models import Profile, Patient
# from profileHub.models import EditProfile
#from appointment.models import Appointment
#from reports.models import ReportsSummaries
#Import Controllers
# from profileHub import specialistController
# from profileHub import patientController



@login_required
def getPatient(request):
    if request.user.is_authenticated:
        userData = Profile.objects.get(user=request.user)
        patientData = Patient.objects.filter(profile=userData.profileID)

        if (patientData):
            context = {'type': userData.type,
                    'firstName': userData.user.first_name,
                    'lastName': userData.user.last_name,
                    'email': userData.user,
                    'birthday': userData.birthday,
                    'phone': userData.phone,
                    'address': userData.address,
                    'image': userData.image,
                    'guardianEmail': patientData,                    
                    }
        else:
            context = {'type': userData.type,
                    'firstName': userData.user.first_name,
                    'lastName': userData.user.last_name,
                    'email': userData.user,
                    'birthday': userData.birthday,
                    'phone': userData.phone,
                    'address': userData.address,
                    'image': userData.image,
                    }
        # return HttpResponse(userData.type)
        return render(request, 'profile.html', context=context)
    return HttpResponse("You do not have permission to view this entrsy.")

@login_required
def patientEdit(request):
    # return render(request,'editProfile.html')
    userData = Profile.objects.get(user=request.user)
    patientData = Patient.objects.filter(profile=userData.profileID)

    if (patientData):
        context = {'type': userData.type,
                'firstName': userData.user.first_name,
                'lastName': userData.user.last_name,
                'email': userData.user,
                'birthday': userData.birthday,
                'phone': userData.phone,
                'address': userData.address,
                'image': userData.image,
                'sex': userData.sex,
                'securityQuestion': userData.securityQuestion,
                'securityAnswer': userData.securityAnswer,
                'guardianEmail': patientData,                    
                }
    else:
        context = {'type': userData.type,
                'firstName': userData.user.first_name,
                'lastName': userData.user.last_name,
                'email': userData.user,
                'birthday': userData.birthday,
                'phone': userData.phone,
                'address': userData.address,
                'image': userData.image,
                'sex': userData.sex,
                'securityQuestion': userData.securityQuestion,
                'securityAnswer': userData.securityAnswer,                
                }
    # return HttpResponse(userData.type)
    return render(request, 'editProfile.html', context=context)
    return HttpResponse("You do not have permission to view this entrsy.")
