from django.contrib import admin

from .models import Patient, PatientList, Specialist, User

admin.site.register(User)
admin.site.register(Specialist)
admin.site.register(Patient)
admin.site.register(PatientList)
