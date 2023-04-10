from django.db import models
from django.contrib.auth.models import User
import uuid

from django.utils import timezone

from registration.models import Patient


class SteppingStone(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stress_level = models.IntegerField(null=True)
    mood_level = models.IntegerField(null=True)
    # Coping Strategies
    personal = models.IntegerField(null=True)
    social = models.IntegerField(null=True)
    sleep = models.IntegerField(null=True)
    actions = models.IntegerField(null=True)
    food = models.IntegerField(null=True)
    score = models.IntegerField(null=True)
    # Keywords
    keywords = models.TextField(null=True)
    anger = models.IntegerField(null=True)
    anticipation = models.IntegerField(null=True)
    joy = models.IntegerField(null=True)
    trust = models.IntegerField(null=True)
    fear = models.IntegerField(null=True)
    surprise = models.IntegerField(null=True)
    sadness = models.IntegerField(null=True)
    disgust = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.patient.profile.user.username} - {self.keyword_id}"


class Keyword(models.Model):
    steppingStones = models.ForeignKey(SteppingStone, on_delete=models.CASCADE)
    wordValue = models.IntegerField(null=True)
    word = models.CharField(max_length=100, null = True)
    wordCategory = models.CharField(max_length=100, null = True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.keyword_id} - {self.keyword}"
