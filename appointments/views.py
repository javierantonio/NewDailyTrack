import datetime
import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect, render
from patientDirectory.models import PatientList
from registration.models import Profile, Specialist, Patient
from .models import Appointments, DeclinedAppointments, AcceptedAppointments, RescheduledAppointments
from .appointmentForm import SpecialistAppointmentForm
from django.contrib.auth.models import User

def landingAppointments(request):
    return render(request, 'appointmentsBase.html')

def specialistCalendarView(request):
    userProfile = Profile.objects.get(user=request.user)
   

    # patientList = PatientList.objects.filter(specialist = Specialist.objects.get(profile = userProfile))

    # filteredList = [person.patient.profile for person in patientList]

    # form.setSelectedPatient(PatientList.objects.filter(specialist = Specialist.objects.get(profile = userProfile)))
    
    # form.fields['patient'].queryset = filteredList
    # form.fields['patient'].to_field_name = 'patient'

    if request.method == 'POST':
        SpecialistAppointmentForm(request,Specialist.objects.get(profile = userProfile))

    #     form = SpecialistAppointment()
    #     print(request.POST['patient'])
    #     patientProfile = Profile.objects.get(user = User.objects.get(email = request.POST['patient']))
    #     form.fields['patient'] = Patient.objects.get(profile = patientProfile)
    #     form.setSelectedPatient(selectedPatient = Patient.objects.get(profile = patientProfile))
    #     form = SpecialistAppointment(request.POST)
    #     if form.is_valid():
    #         event = form.save(commit=False) 
    #         event.specialist = request.user  # Set the user field
    #         event.save()
    #         form = SpecialistAppointment()
    else:    
        appointments = getSpecialistAppointments(Specialist.objects.get(profile = userProfile))

    # form.setPatientList(specialist = Specialist.objects.get(profile = userProfile))
    return render(request, 'appointmentCalendar.html', context={'scheduledAppointments': appointments})
    return JsonResponse(getSpecialistAppointments(Specialist.objects.get(profile = userProfile)), safe=False)
    # return JsonResponse(getSpecialistAppointments(Specialist.objects.get(profile = userProfile)), safe=False)
    # if (userProfile.type == 'Specialist'):
    #     return render(request, 'appointmentCalendar.html', getSpecialistAppointments(Specialist.objects.get(profile = userProfile)))
    # elif (userProfile.type == 'Patient'):
    #     render(request, 'appointmentCalendar.html', context=getPatientAppointments(userProfile))

# def querysetPatients(specialistProfile):
#     list = PatientList.objects.filter(specialist = Specialist.objects.get(profile = specialistProfile))
#     patientArray = []
#     for item in list:
#         patientData = Patient.objects.get(profile = item.patient)
#         patientArray.append({
#             'fields': patientData
#             'model'
#         })

def createAppointment(request):
    specialistDetails = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    if request.method == 'POST':
        if SpecialistAppointmentForm(request, specialistDetails)==True:
            return redirect('appointmentCalendar')
        else:
            return redirect('appointmentCalendar')    
    else:          
        list = PatientList.objects.filter(specialist = specialistDetails)
        patientsList = [person.patient for person in list]
        print(patientsList)
        return render(request, 'appointmentCreate.html', context={'patients': patientsList})

def getSpecialistAppointments(specialistId):
    appointments = Appointments.objects.filter(specialist = specialistId)
    scheduledAppointments = []
    for element in appointments:   
        data = {
            'id': element.uuid,
            'specialist': element.specialist.profile.user.first_name+' '+element.specialist.profile.user.last_name,
            'patient': element.patient.profile.user.first_name+' '+element.patient.profile.user.last_name,
            'start': serializeDatetime(element.appointmentStart),
            'end': serializeDatetime(element.appointmentEnd),
            'note': element.note,
            'status': element.status,
        }
        scheduledAppointments.append(data)

    return json.dumps(scheduledAppointments)

def getPatientAppointments(specialistId):
    appointments = Appointments.objects.filter(specialist = specialistId)
    scheduledAppointments = {}
    index = 0
    for element in appointments:
        
        scheduledAppointments[index] = {
            'uuid': element.uuid,
            'specialist': element.specialist,
            'patient': element.patient,
            'appointmentStart': element.appointmentStart,
            'appointmentEnd': element.appointmentEnd,
            'note': element.note,
            'status': element.status,
        }
        
        index+=1

    return scheduledAppointments

def serializeDatetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    else:
        raise TypeError("Object not serializable")

# def createAppointment(request):
#     return render(request, 'appointmentCreate.html')
