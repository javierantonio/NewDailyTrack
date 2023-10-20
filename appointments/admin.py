from django.contrib import admin
from .models import Appointments, DeclinedAppointments, AcceptedAppointments, RescheduledAppointments

admin.site.register(Appointments)
admin.site.register(DeclinedAppointments)
admin.site.register(AcceptedAppointments)
admin.site.register(RescheduledAppointments)