from datetime import datetime
import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect, render
from patientDirectory.models import PatientList
from registration.models import Profile, Specialist, Patient
from .models import Appointments, DeclinedAppointments, AcceptedAppointments, RescheduledAppointments
from .appointmentForm import SpecialistAppointmentForm, PatientAppointmentForm, ConfirmAppointment, DeclineAppointment, ReschedAppointment
from django.contrib.auth.models import User

def landingAppointments(request):
    return render(request, 'appointmentsBase.html')

def calendarView(request):
    userProfile = Profile.objects.get(user=request.user)

    # if request.method == 'POST':
    #     appointmentSelected = request.POST['appointment']
    #     appointmentObject = Appointments.objects.get(uuid = appointmentSelected)
    #     print(appointmentObject)

    # else:    
    appointments = getAppointments(userProfile, 'json')
    print(appointments)
    # form.setPatientList(specialist = Specialist.objects.get(profile = userProfile))
    return render(request, 'appointmentCalendar.html', context={'scheduledAppointments': appointments, 'active': 'calendar','userType':userProfile.type})
    
def createAppointment(request):
    userProfile = Profile.objects.get(user=request.user)   
    
    if request.method == 'POST':
        if(userProfile.type=='Specialist'):
            createForm = SpecialistAppointmentForm(request)             
        else:
            createForm =  PatientAppointmentForm(request)
        #After creating record
        if createForm==True:
            return redirect('appointmentCalendar')
        else:
            return redirect('appointmentCalendar') 
    else:    
        if(userProfile.type=='Specialist'):      
            list = PatientList.objects.filter(specialist = Specialist.objects.get(profile = userProfile))
            usersList = [person.patient for person in list]
        else:
            list = PatientList.objects.filter(patient = Patient.objects.get(profile=userProfile))
            usersList = [person.specialist for person in list]     
        print(usersList)
        return render(request, 'appointmentCreate.html', context={'recipients': usersList, 'active': 'create', 'userType':userProfile.type})

def getAppointments(userProfile, returnType):
    try:
        if(userProfile.type=='Specialist'):
            appointments = Appointments.objects.filter(specialist = Specialist.objects.get(profile = userProfile))
        else:
            appointments = Appointments.objects.filter(patient = Patient.objects.get(profile = userProfile))
        
        scheduledAppointments = []
        for element in appointments:           
            dateAppointment = element.appointmentStart
            data = {            
                'id': element.uuid,
                'user': element.specialist.profile.user.first_name+' '+element.specialist.profile.user.last_name,
                'attendee': element.patient.profile.user.first_name+' '+element.patient.profile.user.last_name,
                # 'specialist': element.specialist.profile.user.first_name+' '+element.specialist.profile.user.last_name,
                # 'patient': element.patient.profile.user.first_name+' '+element.patient.profile.user.last_name,
                # 'date': element.appointmentStart,
                'date': (element.appointmentStart).strftime("%B %d, %Y"),
                'start': (element.appointmentStart).strftime("%Y-%m-%d %H:%M:%S"),
                'end': (element.appointmentEnd).strftime("%Y-%m-%d %H:%M:%S"),
                'note': checkNull(element.note),
                'status': translateStatus(element.status, dateAppointment),
                'createdBy': checkNull(element.createdBy.user.first_name+' '+element.createdBy.user.last_name)
            }
            scheduledAppointments.append(data)
            if(userProfile.type=='Patient'):
                data['user'] = element.patient.profile.user.first_name+' '+element.patient.profile.user.last_name
                data['attendee'] = element.specialist.profile.user.first_name+' '+element.specialist.profile.user.last_name
    
        if returnType == 'json':
            return json.dumps(scheduledAppointments)
        else:
            return scheduledAppointments
    except:
        scheduledAppointments = [
                {            
                'id':'',
                'user':'',
                'attendee':'',
                # 'specialist':'',
                # 'patient':'',
                # 'date':'',
                'date':'',
                'start':'',
                'end':'',
                'note':'',
                'status':'',
                'createdBy':'',
                }
            ]
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
    appointments = getAppointments(userProfile, 'array')

    # for data in appointments:
    #     data['start'] = data['start'].

    return render(request, 'appointmentHistory.html', context={'scheduledAppointments':appointments, 'active': 'history', 'userType':userProfile.type})

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
    userProfile = Profile.objects.get(user=request.user)
    print(userProfile.type)
    if(userProfile.type=='Specialist'):
        userDetails = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    else:
        userDetails = Patient.objects.get(profile = Profile.objects.get(user=request.user))
    appointment = Appointments.objects.get(uuid = request.POST['data'])
    if request.method == 'POST':
        if ConfirmAppointment(appointment, userDetails)==True:
            appointment.status = 'A'
            appointment.save()
        return JsonResponse({'message': 'Appointment Confirmed!'})
    return JsonResponse({'error': 'Invalid request method'})  
    # else:          
        # list = PatientList.objects.filter(specialist = specialistDetails)
        # patientsList = [person.patient for person in list]        
        # return render(request, 'appointmentCreate.html', context={'patients': patientsList, 'active': 'create'})

def declineAppointment(request):
    userProfile = Profile.objects.get(user=request.user)
    if(userProfile.type=='Specialist'):
        userDetails = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    else:
        userDetails = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    appointment = Appointments.objects.get(uuid = request.POST['id'])
    if request.method == 'POST':
        if DeclineAppointment(appointment, request.POST['data'], userDetails)==True:
            appointment.status = 'D'
            appointment.save()
        return JsonResponse({'message': 'Appointment Declined!'})
    return JsonResponse({'error': 'Invalid request method'})  

def rescheduleAppointment(request):
    # ReschedAppointment
    print(request.POST)
    profile = Profile.objects.get(user=request.user)
    data = {
        'id': request.POST['id'],
        'date': request.POST['data[date]'],
        'timeStart': request.POST['data[timeStart]'],
        'timeEnd': request.POST['data[timeEnd]'],
        'reason': request.POST['data[reason]'],
        'reschedBy': profile,
    }
    
    if ReschedAppointment(data)==True:
        return JsonResponse({'message': 'Appointment Declined!'})
    return JsonResponse({'error': 'Invalid request method'}) 
    # print(request.POST['data[timeStart]'])

def confirmRescheduledAppointment(request):
    print(request.POST)

def declineRescheduledAppointment(request):
    print(request.POST)
