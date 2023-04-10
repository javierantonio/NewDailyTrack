import uuid

from django.db import models


class User(models.Model):
    email = (models.EmailField,)
    password = (models.CharField(max_length=50),)
    firstName = (models.CharField(max_length=30),)
    middleName = (models.CharField(max_length=30),)
    lastName = (models.CharField(max_length=30),)
    sex = (models.CharField(max_length=1),)
    birthday = (models.DateField,)
    phoneNumber = (models.CharField(max_length=11),)
    securityQuestion = (models.CharField(max_length=125),)
    securityAnswer = (models.CharField(max_length=125),)
    createdAt = (models.DateTimeField(auto_now_add=True),)
    updatedAt = models.DateTimeField(auto_now=True)


class Specialist(models.Model):
    specId = (models.UUIDField(default=uuid.uuid4, unique=True, editable=False),)
    licenseNum = (models.CharField(max_length=125),)
    clinicAddress = (models.CharField(max_length=250),)
    licenseExpiry = models.DateField


class Patient(models.Model):
    patId = (models.UUIDField(default=uuid.uuid4, unique=True, editable=False),)
    guardianEmail = models.EmailField(null=True)


class PatientList(models.Model):
    patient = (models.ForeignKey("Patient.patId", on_delete=models.CASCADE),)
    specialist = (models.ForeignKey("Specialist.specId", on_delete=models.CASCADE),)
    status = (
        models.SmallIntegerField(max_length=3),
    )  # 0-Pending,1-Active,2-Inactive,3-Terminated
    createdAt = (models.DateTimeField(auto_now_add=True),)
    updatedAt = models.DateTimeField(auto_now=True)
