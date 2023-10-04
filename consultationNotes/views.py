from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from journal import journalControllers
from journal.models import Journal
from registration.models import Profile

@login_required
def notesHome(request, userId):
    if request.user.is_authenticated:
        userprofile = Profile.objects.get(user=request.user)
        if userprofile.type == "Specialist":
            if request.method == "POST":
                userProfile = request.user.profile
                title = request.POST.get('notesTitle')
                content = request.POST.get('notesContent')
                entry = Journal(user=userProfile, title=title, content=content)
                entry.save()
                return redirect('viewEntries')
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
            print(userprofile.type+'sss')
            if request.method == 'POST':
                return HttpResponse("bleh")
            else:
                print('entries')
                userProfile = request.user.profile
                entries = Journal.objects.filter(user=userId)
                context = {'entries': entries}
                print(entries)
                return render(request, 'entriesNotes.html', context)
        else:
            print(userprofile.type)
            return redirect('landing')
    else:
        return redirect('landing')

