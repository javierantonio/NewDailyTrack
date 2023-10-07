from django.db import models
from django.contrib.auth.models import User
import uuid

class ConsultationNotes(models.Model):
    uuid = models.CharField(primary_key=True, max_length=60, default=uuid.uuid4, editable=False)
    specialist = models.ForeignKey('registration.Profile', null = True, on_delete=models.CASCADE, related_name="specialistProfile")
    patient = models.ForeignKey('registration.Profile', null = True, on_delete=models.CASCADE, related_name="patientProfile")
    notesTitle = models.CharField(max_length=200, null=True)
    notesContent = models.TextField(null=True)
    # sharedWith = models.ManyToManyField(User, blank=True, related_name='sharedWith')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notesTitle
