from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
#Import Models
from registration.models import Profile, Patient, Specialist
from . import profileForms
# from profileHub.models import EditProfile
#from appointment.models import Appointment
#from reports.models import ReportsSummaries
#Import Controllers
# from profileHub import specialistController
# from profileHub import patientController


#PATIENT
@login_required
def getPatient(request):
    if request.user.is_authenticated:
        userData = Profile.objects.get(user=request.user)
        patientData = Patient.objects.get(profile=userData)

        if (patientData):
            context = {'type': userData.type,
                    'firstName': userData.user.first_name,
                    'lastName': userData.user.last_name,
                    'email': userData.user,
                    'birthday': userData.birthday,
                    'phone': userData.phone,
                    'address': userData.address,
                    'image': userData.image,
                    'patientType': patientData.patientType,
                    'guardianEmail': patientData.guardianEmail,                    
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
                    # 'patientType': patientData.patientType,
                    }
        # return HttpResponse(userData.type)
        return render(request, 'profile.html', context=context)
    return redirect('landing')

@login_required
def editPatient(request):
    # return render(request,'editProfile.html')
    userData = Profile.objects.get(user=request.user)
    patientData = Patient.objects.get(profile=userData.profileID)

    if request.method == 'POST':
        if profileForms.patientUpdate(request):
            print('success')
            return reverse('')
        else:
            print('failed')
    else:
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
    
    return redirect(reverse('patientHub'))
    return HttpResponse("You do not have permission to view this entrsy.")

#SPECIALIST
@login_required
def getSpecialist(request):
    if request.user.is_authenticated:
        userData = Profile.objects.get(user=request.user)
        specialistData = Specialist.objects.get(profile=userData)
        # return HttpResponse(specialistData)
        context = {
            'type': userData.type,
            'firstName': userData.user.first_name,
            'lastName': userData.user.last_name,
            'email': userData.user,
            'birthday': userData.birthday,
            'phone': userData.phone,
            'address': userData.address,
            'image': userData.image,
            'licenseNumber': specialistData.licenseNumber,
            'licenseExpiry': specialistData.licenseExpiry,
            'prcID': specialistData.prcID,
            'specialistType': specialistData.specialistType,                    
        }
        return render(request, 'profile.html', context=context)
    return HttpResponse("You do not have permission to view this entrsy.")

@login_required
def editSpecialist(request):
    userData = Profile.objects.get(user=request.user)
    specialistData = Specialist.objects.get(profile=userData)

    if request.method == 'POST':
            if profileForms.specialistUpdate(request):
                print('success')
                return reverse('')
            else:
                print('failed')
    else:
        context = {
            'type': userData.type,
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
            'licenseNumber': specialistData.licenseNumber,
            'licenseExpiry': specialistData.licenseExpiry,
            'prcID': specialistData.prcID,                 
        }
        # return HttpResponse(userData.type)
        return render(request, 'editProfile.html', context=context)
    return redirect(reverse('specialistHub'))

