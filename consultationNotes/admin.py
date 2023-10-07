from django.contrib import admin

from consultationNotes.models import ConsultationNotes


# Register your models here.

class ConsultationNotesAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'specialist', 'patient', 'notesTitle', 'notesContent', 'created_at', 'updated_at')
    list_display_links = ('uuid', 'notesTitle')


admin.site.register(ConsultationNotes)
