from django.contrib import admin
from patientDirectory.models import Enrollment, PatientList

# Register your models here.

admin.site.register(Enrollment)
admin.site.register(PatientList)
