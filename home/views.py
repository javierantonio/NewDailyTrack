from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from registration.models import Profile
import patientDashboard.urls

# Create your views here.

def landing(request):
    if request.user.is_authenticated:

        userprofile = Profile.objects.get(user=request.user)
        print(userprofile.type)
        context = {
            'userprofile': userprofile,
            'user': request.user,
            # add more profile data as needed
        }

        if userprofile.type == "Patient":
            return render(request, 'patientHome.html', context=context)
        elif userprofile.type == "Specialist":
            # return redirect(reverse('patientDashboardHome'))
            # return HttpResponseRedirect('patientDashboard:landing')
            return redirect('patientDashboardHome')

        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
