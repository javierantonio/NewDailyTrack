from django import forms
from .models import Appointments
from patientDirectory.models import PatientList
from django.forms.widgets import DateTimeInput

class SpecialistAppointment(forms.ModelForm):
    patient = forms.ModelChoiceField(
        queryset=PatientList.objects.all(),
        to_field_name='patient',
        required=True,  # You can set this to True or False as needed
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Appointments
        fields = ['appointmentStart', 
                  'appointmentEnd', 
                  'note',
                  'patient']
        labels = {
            'patient': 'Patient Email',
            'appointmentStart': 'Start Date and Time',
            'appointmentEnd': 'End Date and Time',
            'note': 'Notes',            
        }

        widgets = {
            'appointmentStart': forms.DateInput(attrs={'class': 'form-control form-control-user input-daterange'}),
            'appointmentEnd': forms.DateInput(attrs={'class': 'form-control form-control-user input-daterange'}),
        }
