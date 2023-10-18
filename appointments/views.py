import datetime
import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from registration.models import Profile, Specialist
from .models import Appointments, DeclinedAppointments, AcceptedAppointments, RescheduledAppointments

def landingAppointments(request):
    return render(request, 'appointmentsBase.html')

def calendarView(request):
    userProfile = Profile.objects.get(user=request.user)
    appointments = getSpecialistAppointments(Specialist.objects.get(profile = userProfile))
    return render(request, 'appointmentCalendar.html', context={'scheduledAppointments': appointments})
    return JsonResponse(getSpecialistAppointments(Specialist.objects.get(profile = userProfile)), safe=False)
    # return JsonResponse(getSpecialistAppointments(Specialist.objects.get(profile = userProfile)), safe=False)
    # if (userProfile.type == 'Specialist'):
    #     return render(request, 'appointmentCalendar.html', getSpecialistAppointments(Specialist.objects.get(profile = userProfile)))
    # elif (userProfile.type == 'Patient'):
    #     render(request, 'appointmentCalendar.html', context=getPatientAppointments(userProfile))

def getSpecialistAppointments(specialistId):
    appointments = Appointments.objects.filter(specialist = specialistId)
    scheduledAppointments = []
    for element in appointments:        
        data = {
            'id': element.uuid,
            'specialist': element.specialist.profile.profileID,
            'patient': element.patient.profile.profileID,
            'start': serializeDatetime(element.appointmentStart),
            'end': serializeDatetime(element.appointmentEnd),
            'note': element.note,
            'status': element.status,
        }
        scheduledAppointments.append(data)

    return JsonResponse(json.dumps(scheduledAppointments), safe=False)

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


