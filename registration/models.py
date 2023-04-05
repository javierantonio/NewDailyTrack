import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileID = models.CharField(max_length=12, primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=150, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
    type = models.CharField(max_length=10, null=True)
    sex = models.CharField(max_length=10, null=True)
    birthday = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=150, null=True)
    securityQuestion = models.CharField(max_length=150, null=True)
    securityAnswer = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.user.username


class Specialist(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    licenseNumber = models.CharField(max_length=20, null=True)
    licenseExpiry = models.DateField(null=True)
    prcID = models.ImageField(default='default.jpg', upload_to='prc_pics', null=True)

    def __str__(self):
        return self.profile.user.username


