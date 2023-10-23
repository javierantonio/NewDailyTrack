from datetime import datetime, date
from django import forms
from .models import Appointments
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

def SpecialistAppointmentForm(request, specialist):
    patients = PatientList.objects.filter(specialist=specialist)
    if request.method == 'POST':
        patientProfile = Profile.objects.get(user = User.objects.get(email = request.POST['patient']))
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
 
