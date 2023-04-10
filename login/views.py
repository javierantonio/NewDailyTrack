import django
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse
# from django.contrib import messages
from django.contrib.auth.models import User

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
            profile = Profile.objects.get(user=request.user)
            if profile.type == "Specialist":
                return redirect(reverse('landing'))
            elif profile.type == "Patient":
                return redirect(reverse('landing'))
            return HttpResponse("What the fucking hell are you then?!")
        else:
            return render(request, 'login.html')

    else:
        return HttpResponse("Invalid request")


def forgotPassword(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})
