from django.db import models
from django.contrib.auth.models import User

class ConsultationNotes(models.Model):
    user = models.ForeignKey('registration.Profile', on_delete=models.CASCADE)
    notesTitle = models.CharField(max_length=200, null=True)
    notesContent = models.TextField(null=True)
    # sharedWith = models.ManyToManyField(User, blank=True, related_name='sharedWith')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notesTitle
