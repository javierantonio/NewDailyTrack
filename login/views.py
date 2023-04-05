from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages

from registration.models import Profile


# Create your views here.

def loginUser(request):
    return render(request, 'loginTest.html')


def login(request):
    print("Hello")
    if request.method == "POST":
        print("Meow")
        username = request.POST.get('useremail')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            usertype = Profile.objects.get(user=user).type
            print("User is authenticated")
            print(usertype)
            return redirect(reverse('loginUser'), type=usertype)
        else:
            messages.error(request, "Invalid email or password.")
            print("User is not authenticated")
            return HttpResponse("User is not authenticated")

    elif request.method == "GET":
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            if profile.type == "Specialist":
                return redirect(reverse('specialistHome'))
            elif profile.type == "Patient":
                return redirect(reverse('patientHome'))
            return HttpResponse("User is logged in as " + request.user.username )
        else:
            return HttpResponse("User is not logged in")

    else:
        return HttpResponse("Invalid request")