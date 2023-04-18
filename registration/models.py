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
    patientType = models.CharField(max_length=2, null=True)
    #   Different Patient Types and functions
    #   Patients initially either falls into the two categories: UM or UP.
    #       Once an account profile has been created and patient, it automatically sends a verification email to the provided email addresses
    #   1. UM - Unapproved Minor. A minor who has not yet been approved by a guardian. This could be a result of the guardian account not giving a response or denied the request.
    #   2. AM - Approved Minor. A minor who has been approved by a guardian.
    #   3. UP - Unverified Patient. A patient who has not yet had the account verified.1
    #   4. VP - Verified Patient. A patient who has been verified via email.
    guardianEmail = models.EmailField(max_length=150, null=True)

    def __str__(self):
        return self.profile.user.username


class Specialist(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    licenseNumber = models.CharField(max_length=20, null=True)
    licenseExpiry = models.DateField(null=True)
    prcID = models.ImageField(default='default.jpg', upload_to='prc_pics', null=True)
    specialistType = models.CharField(max_length=2, null=True)
    #   Different Specialist Types and functions
    #   1. U - Unverified. A specialist who has not yet had the account verified.
    #   2. V - Verified. A specialist who has been verified by app moderators.

    def __str__(self):
        return self.profile.user.username


class AdminModerator (models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # Moderators can only access admin view and approve/reject specialist application requests. They decide to verify or not verify the specialist.

    def __str__(self):
        return self.profile.user.username

