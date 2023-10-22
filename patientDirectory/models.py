from django.db import models
import uuid

# Create your models here.
class Enrollment(models.Model):
    specialist = models.ForeignKey('registration.Specialist', on_delete=models.CASCADE, related_name='enrollments')
    patientEmail = models.EmailField(max_length=254, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enrollmentCode = models.CharField(max_length=6, unique=True, default=uuid.uuid4().hex[:6])
        #   Auto generates a 6 digit code for the patient to enter in the app to verify the enrollment
    enrollmentStatus = models.CharField(max_length=2, null=True)
        #   Different Enrollment Status and functions
        #   1. P - Pending. A patient who has not yet availed the code.
        #   2. A - Availed. A patient who has availed the code.
        #   3. T - Terminated. A code that has been terminated by the specialist.

class PatientList(models.Model):
    specialist = models.ForeignKey('registration.Specialist', on_delete=models.CASCADE, related_name='patientlist')
    patient = models.ForeignKey('registration.Patient', on_delete=models.CASCADE, related_name='patient')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patientListStatus = models.CharField(max_length=2, null=True)
    enrollmentCode = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
        #   Different Patient List Status and functions
        #   1. A - Active. A patient who is currently being monitored by the specialist.
        #   2. I - Inactive. A patient who is no longer being monitored by the specialist.
    def combination(self):
        return f"{self.patient} {self.specialist}"
    
    def __str__(self):
        return self.combination()
