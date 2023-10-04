from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render

from consultationNotes.models import ConsultationNotes
from registration.models import Profile

def processConsultationNotes(request):
    if request.method == 'POST':
        userProfile = request.user.profile
        title = request.POST.get('entryTitle')
        content = request.POST.get('entryContent')
        entry = ConsultationNotes(user=userProfile, notesTitle=title, notesContent=content)
        entry.save()
        print("Consultation Notes Saved")
        return redirect('entriesNotes')

    else:
        return render(request, 'entriesNotes.html')


def viewConsultationNotes(request):
    if request.method == 'POST':
        return HttpResponse("bleh")
    else:
        userProfile = request.user.profile
        entries = ConsultationNotes.objects.get(user=userProfile)
        context = {'entries': entries}
        for entry in entries:
            print(entry.notesTitle)
            print(entry.created_at)
        return render(request, 'entriesNotes.html', context)
