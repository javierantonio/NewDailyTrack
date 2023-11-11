from datetime import datetime
import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect, render
from patientDirectory.models import PatientList
from registration.models import Profile, Specialist, Patient
from .models import Appointments, DeclinedAppointments, AcceptedAppointments, RescheduledAppointments
from .appointmentForm import SpecialistAppointmentForm, ConfirmAppointment, DeclineAppointment
from django.contrib.auth.models import User

def landingAppointments(request):
    return render(request, 'appointmentsBase.html')

def specialistCalendarView(request):
    userProfile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        appointmentSelected = request.POST['appointment']
        appointmentObject = Appointments.objects.get(uuid = appointmentSelected)
        print(appointmentObject)

    else:    
        appointments = getSpecialistAppointments(Specialist.objects.get(profile = userProfile), 'json')
        print(appointments)
    # form.setPatientList(specialist = Specialist.objects.get(profile = userProfile))
    return render(request, 'appointmentCalendar.html', context={'scheduledAppointments': appointments, 'active': 'calendar'})
    
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
        return render(request, 'appointmentCreate.html', context={'patients': patientsList, 'active': 'create'})

def getSpecialistAppointments(specialistId, returnType):
    appointments = Appointments.objects.filter(specialist = specialistId)
    scheduledAppointments = []
    for element in appointments:           
        dateAppointment = element.appointmentStart
        data = {            
            'id': element.uuid,
            'user': element.specialist.profile.user.first_name+' '+element.specialist.profile.user.last_name,
            'attendee': element.patient.profile.user.first_name+' '+element.patient.profile.user.last_name,
            # 'specialist': element.specialist.profile.user.first_name+' '+element.specialist.profile.user.last_name,
            # 'patient': element.patient.profile.user.first_name+' '+element.patient.profile.user.last_name,
            'start': (element.appointmentStart).strftime("%Y-%m-%d %H:%M:%S"),
            'end': (element.appointmentEnd).strftime("%Y-%m-%d %H:%M:%S"),
            'note': checkNull(element.note),
            'status': translateStatus(element.status, dateAppointment),
            'createdBy': checkNull(element.createdBy.user.first_name+' '+element.createdBy.user.last_name)
        }
        scheduledAppointments.append(data)

    if returnType == 'json':
        return json.dumps(scheduledAppointments)
    else:
        return scheduledAppointments

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
            'status': translateStatus(element.status),
        }
        
        index+=1

    return scheduledAppointments

def serializeDatetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    else:
        raise TypeError("Object not serializable")

def appointmentHistory(request):
    userProfile = Profile.objects.get(user=request.user)
    appointments = getSpecialistAppointments(Specialist.objects.get(profile = userProfile), 'array')

    return render(request, 'appointmentHistory.html', context={'scheduledAppointments':appointments, 'active': 'history'})

# def createAppointment(request):
#     return render(request, 'appointmentCreate.html')

def translateStatus(status, date):
    inputDate = date.date()
    currentDate = datetime.now().date()

    if status == 'P' and inputDate>currentDate:
        return 'Pending'
    elif status == 'A':
        return 'Confirmed'
    elif status == 'R':
        return 'Rescheduled'
    elif status == 'D':
        return 'Declined'
    else:
        return 'Cancelled'
    
def checkNull(data):
    if data:
        return data
    else:
        return 'None'
    
# def checkRecipient(data, user):
#     if data == user:
#         return element.patient.profile.user.first_name+' '+element.patient.profile.user.last_name,

def confirmAppointment(request):
    specialistDetails = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    appointment = Appointments.objects.get(uuid = request.POST['data'])
    if request.method == 'POST':
        if ConfirmAppointment(appointment, specialistDetails)==True:
            appointment.status = 'A'
            appointment.save()
        return JsonResponse({'message': 'Appointment Confirmed!'})
    return JsonResponse({'error': 'Invalid request method'})  
    # else:          
        # list = PatientList.objects.filter(specialist = specialistDetails)
        # patientsList = [person.patient for person in list]        
        # return render(request, 'appointmentCreate.html', context={'patients': patientsList, 'active': 'create'})

def declineAppointment(request):
    specialistDetails = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    appointment = Appointments.objects.get(uuid = request.POST['id'])
    if request.method == 'POST':
        if DeclineAppointment(appointment, request.POST['data'], specialistDetails)==True:
            appointment.status = 'D'
            appointment.save()
        return JsonResponse({'message': 'Appointment Declined!'})
    return JsonResponse({'error': 'Invalid request method'})  

def rescheduleAppointment(request):
    print(request.POST)

def confirmRescheduledAppointment(request):
    print(request.POST)

def declineRescheduledAppointment(request):
    print(request.POST)
