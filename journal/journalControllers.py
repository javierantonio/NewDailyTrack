from django.forms import forms
from django.shortcuts import redirect, render

from journal.models import Journal
from registration.models import Profile


def processJournalEntry(request):
    if request.method == 'POST':
        userProfile = request.user.profile
        title = request.POST.get('entryTitle')
        content = request.POST.get('journalContent')
        entry = Journal(user=userProfile, title=title, content=content)
        entry.save()
        print("Journal Entry Saved")
        return redirect('journalHome')

    else:
        return render(request, 'journalHome.html')
