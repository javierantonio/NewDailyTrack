from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
#Import Models
from registration.models import Profile, Patient, Specialist
from . import profileForms
from patientDirectory.models import Enrollment, PatientList
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
        if(request.method == "POST"):
            try:
                enrolledAccount = Enrollment.objects.get(enrollmentCode = request.POST['enrollmentCode'])
                try:
                    if (PatientList.objects.get(specialist = enrolledAccount.specialist, patient = patientData, patientListStatus = 'A')):
                        print("account already registered to the specialist")
                except ObjectDoesNotExist:
                    registerSpecialist(enrolledAccount, patientData)
            except:
                print("code doesn't exist")
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
            return render(request, 'profile.html', context={'data':context, 'specialistsData': getRegisteredSpecialists(userData.user)})
    return redirect('landing')

@login_required
def editPatient(request):
    # return render(request,'editProfile.html')
    userData = Profile.objects.get(user=request.user)
    patientData = Patient.objects.get(profile=userData.profileID)

    if request.method == 'POST':
        if profileForms.patientUpdate(request):
            print('success')
            return redirect(reverse('login'))
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
        return render(request, 'editProfile.html', context)
    
    return redirect(reverse('patientHub'))
    return HttpResponse("You do not have permission to view this entrsy.")

#SPECIALIST
@login_required
def getSpecialist(request):
    if request.user.is_authenticated:
        userData = Profile.objects.get(user=request.user)
        specialistData = Specialist.objects.get(profile=userData)
        # return HttpResponse(specialistData)
        if(request.method == "POST"):
            addPatient(request.POST['patientEmail'], userData)
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
        return render(request, 'profile.html', context={'data':context,'patientsData':getPatientDirectory(request.user)})
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

def getPatientDirectory(userData):
    specialistId = Specialist.objects.get(profile = Profile.objects.get(user=userData))
    allInvitedPatients = Enrollment.objects.filter(specialist = specialistId).order_by('created_at')
    pendingInvitedPatients = Enrollment.objects.filter(specialist = specialistId, enrollmentStatus = 'P').order_by('created_at')
    patientsList = PatientList.objects.filter(specialist = specialistId).order_by('created_at')
    registeredPatients = {}
    index = 0
    for element in patientsList:
        patientDetails = Profile.objects.get(email = element.patient)
        registeredPatients[index] = {
            'patientName': patientDetails.user.first_name+' '+patientDetails.user.last_name,
            'created_at': element.created_at,
            'enrollmentCode': element.enrollmentCode.enrollmentCode,
            'status': element.patientListStatus
        }
        index+=1
    return [pendingInvitedPatients, allInvitedPatients, registeredPatients]

def getRegisteredSpecialists(userData):
    specialistArray = {}
    index = 0
    patientId = Patient.objects.get(profile = Profile.objects.get(user=userData))
    patientList = PatientList.objects.filter(patient = patientId).order_by('created_at')
    
    for element in patientList:
        specialistDetails = Profile.objects.get(email = element.specialist)
        specialistArray[index] = {
            'enrollmentCode': element.enrollmentCode.enrollmentCode,
            'specialistName': specialistDetails.user.first_name+' '+specialistDetails.user.last_name,
            'contactNumber': specialistDetails.phone,
            'email': specialistDetails.email,
            'dateStarted': element.created_at,
            'status': element.patientListStatus,
        }
        index+=1
    return specialistArray

#PATIENT MANAGEMENT
def addPatient(patientEmail, userProfile):
    try:
        newPatient = Enrollment.objects.create(
            specialist = Specialist.objects.get(profile = userProfile),
            patientEmail = patientEmail,
            enrollmentStatus = "P"
        )
        newPatient.save()
        print('SUCCESS')
    except Exception as e:
        print(e)
        
def registerSpecialist(enrolledAccount, patientDetails):
    try:     
        # if (PatientList.objects.get(specialist = enrolledAccount.specialist, patient = patientDetails))
        if (enrolledAccount.enrollmentStatus == "P"):
            enrolledAccount.enrollmentStatus = "A"

            newPatient = PatientList.objects.create(
                specialist = enrolledAccount.specialist,
                patient = patientDetails,
                patientListStatus = "A",
                enrollmentCode = enrolledAccount
            )

            enrolledAccount.save()
            newPatient.save()
            print('SUCCESS')
        else:
            print('code no longer available')
    except Exception as e:
        print(e)

def removeInvitedPatient(request):
    invitedPatient = Enrollment.objects.get(enrollmentCode = request.POST['code'])
    invitedPatient.enrollmentStatus = 'T'
    invitedPatient.save()
    return redirect('specialistHub')

def removeRegisteredPatient(request):
    patient = PatientList.objects.get(enrollmentCode = get_object_or_404(Enrollment, enrollmentCode=request.POST['code']))
    patient.patientListStatus = 'I'
    patient.save()
    return redirect('landing')
    