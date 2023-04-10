from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.

def logoutUser(request):
    logout(request)
    request.session.flush()
    return redirect(reverse('landing'))