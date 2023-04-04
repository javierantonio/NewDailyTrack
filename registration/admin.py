from django.contrib import admin

from registration.models import Profile, Patient, Specialist

# Register your models here.

admin.site.register(Profile)
admin.site.register(Patient)
admin.site.register(Specialist)
