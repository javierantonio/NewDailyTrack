from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError
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
            patientProfile = Profile.objects.get(profileID = userId)
            print(userprofile, patientProfile)
            if request.method == "POST":                 
                try:
                    # Get existing Profile instances or create new ones
                    specialist_profile = Profile.objects.get(profileID = userprofile.profileID)
                    patient_profile = Profile.objects.get(profileID = userId)  
                    
                    consultation_notes = ConsultationNotes.objects.create(
                        specialist=specialist_profile,
                        patient=patient_profile,
                        notesTitle = request.POST.get('entryTitle'),
                        notesContent = request.POST.get('entryContent')
                    )
                    print(consultation_notes)
                    consultation_notes.save()
                except IntegrityError as e:
                    print(f"IntegrityError: {e}")
                return redirect(reverse('noteView', kwargs={'userId': userId}))
            elif request.method == "GET":
                return render(request, 'composeNotes.html', context={'patient': patientProfile})
        else:
            return redirect('landing')
    else:
        return redirect('landing')
    
# def notesHome(request):
#     if request.user.is_authenticated:
#         userprofile = Profile.objects.get(user=request.user)
#         if userprofile.type == "Specialist":
#             if request.method == "POST":
#                 userProfile = request.user.profile
#                 title = request.POST.get('entryTitle')
#                 content = request.POST.get('entryContent')
#                 entry = ConsultationNotes(user=userProfile, notesTitle=title, notesContent=content)
#                 entry.save()
#                 return redirect(reverse('notesEntries'))
#             elif request.method == "GET":
#                 return render(request, 'composeNotes.html')
#         else:
#             return redirect('landing')
#     else:
#         return redirect('landing')
    
@login_required
def viewEntries(request, userId):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if "Specialist" in userprofile.type:
            if request.method == 'POST':
                return HttpResponse("bleh")
            else:
                print('entries')
                patientProfile = Profile.objects.get(profileID = userId)
                entries = ConsultationNotes.objects.filter(specialist=userprofile, patient=patientProfile)
                context = {'entries': entries, 'patient':patientProfile}
                return render(request, 'entriesNotes.html', context)
        else:
            print(patientProfile.type)
            return redirect('landing')
    else:
        return redirect('landing')

@login_required
def deleteNotes(request, entryId):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Specialist":
            if request.method == 'GET':
                notesEntry = ConsultationNotes.objects.get(uuid=entryId)
                # patientProfile = Profile.objects.get(profileID = notesEntry.patient)
                # if patientProfile == notesEntry.user:
                notesEntry.delete()
                return redirect(reverse('noteView', kwargs={'userId': notesEntry.patient.profileID}))
        else:
            return redirect('landing')
    else:
        return redirect('landing')

@login_required
def openEntry(request, entryId, userId):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Specialist":            
            if request.method == 'GET':
                patientProfile = Profile.objects.get(profileID = userId)
                notesEntry = ConsultationNotes.objects.get(uuid=entryId)
                return render(request, 'viewNote.html', context={'patient': patientProfile,
                                                                 'notesEntry': notesEntry} )
            return redirect(reverse('noteView', kwargs={'userId': userId}))
        else:
            return redirect('landing')
    else:
        return redirect('landing')
