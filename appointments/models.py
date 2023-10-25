from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from registration.models import Profile, Specialist, Patient

class Appointments(models.Model) :
    uuid = models.CharField(primary_key=True, max_length=60, default=uuid.uuid4, editable=False)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    appointmentStart = models.DateTimeField(null=True)
    appointmentEnd = models.DateTimeField(null=True)    
    note = models.TextField(max_length=1500, blank=True, null=True)
    status = models.CharField(default='P', max_length=10, null=True)
    # Pending, Accepted, Declined, Rescheduled    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RescheduledAppointments(models.Model):
    oldAppointment = models.ForeignKey(Appointments, on_delete=models.CASCADE, related_name='oldAppointment')
    newAppointment = models.ForeignKey(Appointments, on_delete=models.CASCADE, related_name='newAppointment')
    rescheduledBy = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=True)
    #Pending, Accepted, Declined
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DeclinedAppointments(models.Model):
    appointment = models.ForeignKey(Appointments, on_delete=models.CASCADE)
    declinedBy = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reason = models.CharField(max_length=1500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class AcceptedAppointments(models.Model):
    appointment = models.ForeignKey(Appointments, on_delete=models.CASCADE)
    acceptedBy = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    