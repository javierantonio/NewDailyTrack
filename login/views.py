import django
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

from registration.models import Profile


# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'landing')

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if profile.type == "Specialist":
            return redirect(reverse('specialistHome'))
        elif profile.type == "Patient":
            return redirect(reverse('patientHome'))
        return HttpResponse("User is logged in as " + request.user.username)

    return render(request, 'userSelect.html')


def loginUser(request):
    return render(request, 'loginTest.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('useremail')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return redirect(reverse('landing'))
        else:
            return HttpResponse("User is not authenticated")

    elif request.method == "GET":
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                if profile.type == "Specialist":
                    return redirect(reverse('landing'))
                elif profile.type == "Patient":
                    return redirect(reverse('landing'))
                return HttpResponse("What the fucking hell are you then?!")
            except Profile.DoesNotExist:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')

    else:
        return HttpResponse("Invalid request")


def passwordRecovery(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('changePassword')
    else:
        form = PasswordResetForm()
    return render(request, 'passwordRecovery.html', {'form': form})

def changePassword(request):
    if request.method == "POST":
        return render(request, 'changePassword.html')
        # useremail = request.POST.get('useremail')
        # user = User.objects.get(username = useremail)
        # if user is not None:
        #     return render(request, 'changePassword.html')
        # else:
        #     return HttpResponse("User is not authenticated")
    else:
        return HttpResponse("Invalid request")

def securityQuestions(request):
    return render(request, 'securityQuestions.html')
    # if request.method == 'POST':
    #     form = PasswordResetForm(request.POST)
    #     if form.is_valid():
    #         form.save(request=request)
    #         return redirect('changePassword')
    # else:
    #     form = PasswordResetForm()
    # return render(request, 'passwordRecovery.html', {'form': form})

def newPassword(request):
    return render(request, 'login.html')
