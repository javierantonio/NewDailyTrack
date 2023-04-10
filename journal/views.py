from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from journal import journalControllers
from journal.models import Journal
from registration.models import Profile


# Create your views here.

@login_required
def journalHome(request):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Patient":
            if request.method == "POST":
                userProfile = request.user.profile
                title = request.POST.get('entryTitle')
                content = request.POST.get('journalContent')
                entry = Journal(user=userProfile, title=title, content=content)
                entry.save()
                return redirect('journalEntries')
            elif request.method == "GET":
                return render(request, 'journalHome.html')
        else:
            return redirect('landing')
    else:
        return redirect('landing')


@login_required
def journalEntries(request):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Patient":
            if request.method == 'POST':
                return HttpResponse("bleh")
            else:
                userProfile = request.user.profile
                entries = Journal.objects.filter(user=userProfile)
                context = {'entries': entries}
                return render(request, 'journalEntries.html', context)
        else:
            return redirect('landing')
    else:
        return redirect('landing')


@login_required
def starredJournalEntry(request):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Patient":
            if request.method == 'POST':
                entry_id = request.POST.get('entry_id')
                entry = Journal.objects.get(id=entry_id)
                entry.isStarred = not entry.isStarred
                entry.save()
                data = {
                    'is_starred': entry.isStarred,
                }
                return JsonResponse(data)
            else:
                userProfile = request.user.profile
                entries = Journal.objects.filter(user=userProfile, isStarred=True)
                context = {'entries': entries}
                return render(request, 'journalStarredEntries.html', context)
        else:
            return redirect('landing')
    else:
        return redirect('landing')


@login_required
def deleteJournalEntry(request, entry_id):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Patient":
            if request.method == 'POST':
                return HttpResponse("bleh")
            else:
                journalEntry = Journal.objects.get(id=entry_id)
                if userprofile == journalEntry.user:
                    journalEntry.delete()
                    return redirect('journalEntries')
                return redirect('journalEntries')
        else:
            return redirect('landing')
    else:
        return redirect('landing')

@login_required
def viewJournalEntry(request, entry_id):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Patient":
            if request.method == 'POST':
                return HttpResponse("bleh")
            else:
                journalEntry = Journal.objects.get(id=entry_id)
                if userprofile == journalEntry.user:
                    context = {
                        'journalEntry': journalEntry
                    }
                    return render(request, 'journalViewEntry.html', context)
                return HttpResponse("You do not have permission to view this entry.")
        else:
            return redirect('landing')
    else:
        return redirect('landing')


@login_required
def starJournalEntry(request):
    if request.user.is_authenticated and request.method == 'POST':
        entry_id = request.POST.get('entry_id')
        entry = Journal.objects.get(id=entry_id)
        if request.user.profile == entry.user:
            entry.isStarred = not entry.isStarred
            entry.save()
            return JsonResponse({'is_starred': entry.isStarred})
        else:
            return JsonResponse({'error': 'You do not have permission to update this entry.'})

    return JsonResponse({'error': 'Invalid request'})
