from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from journal import journalControllers
from registration.models import Profile
from home import urls


# Create your views here.


def journalHome(request):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)

        if userprofile.type == "Patient":
            if request.method == "POST":
                return (journalControllers.processJournalEntry(request))
            elif request.method == "GET":
                return render(request, 'journalHome.html')

        else:
            return redirect('landing')

    else:
        return redirect('landing')
