from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . import consultationControllers
from consultationNotes.models import ConsultationNotes
from registration.models import Profile

@login_required
def notesHome(request, userId):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Specialist":
            if request.method == "POST":
                userProfile = request.user.profile
                title = request.POST.get('entryTitle')
                content = request.POST.get('entryContent')
                entry = ConsultationNotes(user=userProfile, notesTitle=title, notesContent=content)
                entry.save()
                return redirect(reverse('notesEntries'))
            elif request.method == "GET":
                return render(request, 'composeNotes.html', context={'user': userId})
        else:
            return redirect('landing')
    else:
        return redirect('landing')
    
@login_required
def viewEntries(request, userId):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if "Specialist" in userprofile.type:
            if request.method == 'POST':
                return HttpResponse("bleh")
            else:
                print('entries')
                userProfile = request.user.profile
                entries = ConsultationNotes.objects.filter(user=userId)
                context = {'entries': entries}
                print(entries)
                return render(request, 'entriesNotes.html', context)
        else:
            print(userprofile.type)
            return redirect('landing')
    else:
        return redirect('landing')

@login_required
def deleteNotes(request, entry_id):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Specialist":
            if request.method == 'POST':
                return HttpResponse("bleh")
            else:
                notesEntry = ConsultationNotes.objects.get(id=entry_id)
                if userprofile == notesEntry.user:
                    notesEntry.delete()
                    return redirect(reverse('notesEntries'))
                return redirect(reverse('notesEntries'))
        else:
            return redirect('landing')
    else:
        return redirect('landing')

@login_required
def viewNotes(request, entry_id):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Specialist":
            if request.method == 'POST':
                return HttpResponse("bleh")
            else:
                notesEntry = ConsultationNotes.objects.get(id=entry_id)
                if userprofile == notesEntry.user:
                    context = {
                        'notesEntry': notesEntry
                    }
                    return render(request, 'viewNote.html', context)
                return HttpResponse("You do not have permission to view this entry.")
        else:
            return redirect('landing')
    else:
        return redirect('landing')

