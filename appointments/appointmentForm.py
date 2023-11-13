from datetime import datetime, date
from django import forms
from .models import Appointments, DeclinedAppointments, AcceptedAppointments, RescheduledAppointments
from patientDirectory.models import PatientList
from registration.models import Profile, Specialist, Patient
from django.forms.widgets import DateTimeInput
from django.contrib.auth.models import User

# class SpecialistAppointment(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(SpecialistAppointment, self).__init__(*args, **kwargs)

#         # # Filter patients associated with the specific specialist
#         # patients = PatientList.objects.filter(specialist=specialist)

#         # # Create a list of (value, display) tuples for the ChoiceField
#         # choices = [(patient.patient, str(patient.patient)) for patient in patients]

#         # self.fields['patient'].choices = choices

#     patient = forms.ModelChoiceField(
#         queryset=PatientList.objects.all().values_list('patient', flat=True).distinct(),
#         required=True,  # You can set this to True or False as needed
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#     class Meta:
#         model = Appointments
#         fields = ['patient',
#                   'appointmentStart', 
#                   'appointmentEnd', 
#                   'note']
#         labels = {
#             'patient': 'Patient Email',
#             'appointmentStart': 'Start Date and Time',
#             'appointmentEnd': 'End Date and Time',
#             'note': 'Notes',            
#         }

#         widgets = {
#             'appointmentStart': forms.DateInput(attrs={'class': 'form-control form-control-user input-daterange'}),
#             'appointmentEnd': forms.DateInput(attrs={'class': 'form-control form-control-user input-daterange'}),
#         }

#     def setPatientList(self, specialist):
#         # super(SpecialistAppointment, self).__init__(*args, **kwargs)
        
#         # Filter patients associated with the specific specialist
#         patients = PatientList.objects.filter(specialist=specialist)

#         choices = [(patient.patient.id, patient.patient, str(patient.patient)) for patient in patients]
        
#         self.fields['patient'] = forms.ChoiceField(
#             choices=choices,
#             required=True,
#             widget=forms.Select(attrs={'class': 'form-control'})
#         )
#     # You can also define a custom method to set the selected country
#     def setSelectedPatient(self, selectedPatient):
#         self.initial['patient'] = selectedPatient

# def SpecialistAppointmentForm(request, specialist):
#     if request.method == 'POST':
#         patientProfile = Profile.objects.get(user = User.objects.get(email = request.POST['recipient']))
#         patient = Patient.objects.get(profile=patientProfile)
#         date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
#         timeStart = datetime.strptime(request.POST['timeStart'], '%H:%M').time()
#         timeEnd = datetime.strptime(request.POST['timeEnd'], '%H:%M').time()


#         # Create a new user
#         try:
#             appointment = Appointments.objects.create(patient=patient, 
#                                         appointmentEnd=datetime.combine(date, timeEnd), 
#                                         appointmentStart=datetime.combine(date, timeStart),
#                                         specialist=specialist,
#                                         note = request.POST['notes'],
#                                         createdBy = specialist.profile
#                                         )
#             appointment.save()
    
#             return True
#         except Exception as e:
#             print(e)
#             return False
 
def PatientAppointmentForm(request):
    specialist = Specialist.objects.get(profile = Profile.objects.get(user = User.objects.get(email = request.POST['recipient'])))
    
    if request.method == 'POST':
        patientProfile = Profile.objects.get(user = request.user)
        patient = Patient.objects.get(profile=patientProfile)
        date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
        timeStart = datetime.strptime(request.POST['timeStart'], '%H:%M').time()
        timeEnd = datetime.strptime(request.POST['timeEnd'], '%H:%M').time()


        # Create a new user
        try:
            appointment = Appointments.objects.create(patient=patient, 
                                        appointmentEnd=datetime.combine(date, timeEnd), 
                                        appointmentStart=datetime.combine(date, timeStart),
                                        specialist=specialist,
                                        note = request.POST['notes'],
                                        createdBy = patientProfile
                                        )
            appointment.save()
    
            return True
        except Exception as e:
            print(e)
            return False

def SpecialistAppointmentForm(request):
    specialist = Specialist.objects.get(profile = Profile.objects.get(user=request.user))
    
    if request.method == 'POST':
        patientProfile = Profile.objects.get(user = User.objects.get(email = request.POST['recipient']))
        patient = Patient.objects.get(profile=patientProfile)
        date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
        timeStart = datetime.strptime(request.POST['timeStart'], '%H:%M').time()
        timeEnd = datetime.strptime(request.POST['timeEnd'], '%H:%M').time()


        # Create a new user
        try:
            appointment = Appointments.objects.create(patient=patient, 
                                        appointmentEnd=datetime.combine(date, timeEnd), 
                                        appointmentStart=datetime.combine(date, timeStart),
                                        specialist=specialist,
                                        note = request.POST['notes'],
                                        createdBy = specialist.profile
                                        )
            appointment.save()
    
            return True
        except Exception as e:
            print(e)
            return False
 
def ConfirmAppointment(appointment, user):
    try:
        appointment = AcceptedAppointments.objects.create(
            appointment = appointment,
            acceptedBy = user.profile
        )
        appointment.save()

        return True
    except Exception as e:
        print(e)
        return False

def DeclineAppointment(appointment, reason, user):
    try:
        appointment = DeclinedAppointments.objects.create(
            appointment = appointment,
            declinedBy = user.profile,
            reason = reason,
        )
        appointment.save()

        return True
    except Exception as e:
        print(e)
        return False

def ReschedAppointment(request):
    # if request.method == 'POST':
    # patientProfile = Profile.objects.get(user = User.objects.get(email = request.POST['patient']))
    # patient = Patient.objects.get(profile=patientProfile)
    date = datetime.strptime(request['date'], '%Y-%m-%d').date()
    timeStart = datetime.strptime(request['timeStart'], '%H:%M').time()
    timeEnd = datetime.strptime(request['timeEnd'], '%H:%M').time()
    reason = request['reason']
    reschedBy = request['reschedBy']

    # if(reschedBy['type']=='Specialist'):

    try:
        oldAppointment = Appointments.objects.get(uuid = request['id'])
        # Create a RescheduledAppointments instance
        rescheduled_appointment = RescheduledAppointments.objects.create(
            oldAppointment=oldAppointment,
            newAppointment=None,  # This will be updated by the duplicate_old_appointment method
            rescheduledBy=reschedBy,
            status='Pending'  # Set the status as needed
        )

        # Duplicate the old appointment and set it as the new appointment
        rescheduled_appointment.duplicate_old_appointment()
        print('donee ')

        rescheduled_appointment.newAppointment.appointmentStart = datetime.combine(date, timeStart)
        rescheduled_appointment.newAppointment.appointmentEnd = datetime.combine(date, timeEnd)
        rescheduled_appointment.newAppointment.note = reason
        rescheduled_appointment.save()

        oldAppointment.status = 'R'
        oldAppointment.save()
    
        return True
    except Exception as e:
        print(e)
        return False

    # try:
        

    #     appointment = Appointments.objects.create(patient=patient, 
    #                                 appointmentEnd=datetime.combine(date, timeEnd), 
    #                                 appointmentStart=datetime.combine(date, timeStart),
    #                                 specialist=specialist,
    #                                 note = request.POST['notes'],
    #                                 createdBy = specialist.profile
    #                                 )
    #     appointment.save()
    
    #     appointment = RescheduledAppointments.objects.create(
    #         oldAppointment = request['oldAppointment'],
    #         newAppointment = request['newAppointment'],
    #         rescheduledBy = user.profile,
    #         status = 'P',
    #     )
    #     appointment.save()

    #     return True
    # except Exception as e:
    #     print(e)
    #     return False

