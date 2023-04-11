from django.db import models
from django.contrib.auth.models import User
import uuid

from django.utils import timezone

from registration.models import Patient


class SteppingStone(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=60, default=uuid.uuid4, editable=False)
    stresslevel = models.IntegerField(null=True)
    moodLevel = models.IntegerField(null=True)
    # Coping Strategies
    personal = models.IntegerField(null=True)
    personalDesc = models.TextField(null=True)
    social = models.IntegerField(null=True)
    socialDesc = models.TextField(null=True)
    sleep = models.IntegerField(null=True)
    sleepDesc = models.TextField(null=True)
    actions = models.IntegerField(null=True)
    actionsDesc = models.TextField(null=True)
    food = models.IntegerField(null=True)
    foodDesc = models.TextField(null=True)
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
        return f"{self.patient} {self.uuid}"


class Keyword(models.Model):
    uuid = models.CharField(max_length=60, default=uuid.uuid4, editable=False)
    wordValue = models.IntegerField(null=True)
    word = models.CharField(max_length=100, null = True)
    wordCategory = models.CharField(max_length=100, null = True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.word} {self.uuid}"
