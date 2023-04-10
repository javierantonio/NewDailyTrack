from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from registration.models import Profile, Patient
from steppingStones.models import SteppingStone


# Create your views here.
def steppingStoneStart(request):
    if request.user.is_authenticated:
        userProfile = Profile.objects.get(user=request.user)
        if userProfile.type == "Patient":
            patient = Patient.objects.get(profile=userProfile)
            if request.method == "POST":
                if request.session['food'] is None and request.session['actions'] is not None:
                    request.session['food'] = request.POST.get('food')
                    return HttpResponse('this is where your score is calculated and emoticard shown.')
                elif request.session['actions'] is None and request.session['sleep'] is not None:
                    request.session['actions'] = request.POST.get('actions')
                    return render(request, 'food.html')
                elif request.session['sleep'] is None and request.session['social'] is not None:
                    request.session['sleep'] = request.POST.get('sleep')
                    return render(request, 'actions.html')
                elif request.session['social'] is None and request.session['personal'] is not None:
                    request.session['social'] = request.POST.get('social')
                    return render(request, 'sleep.html')
                elif request.session['personal'] is None and request.session['keywords'] is not None:
                    request.session['personal'] = request.POST.get('personal')
                    return render(request, 'social.html')
                elif request.session['keywords'] is None and request.session['mood'] is not None:
                    request.session['keywords'] = request.POST.get('keywords')
                    return render(request, 'personal.html')
                elif request.session['mood'] is None and request.session['stressLevel'] is not None:
                    request.session['mood'] = request.POST.get('mood')
                    return render(request, 'keywords.html')
                elif request.session['stressLevel'] is None:
                    request.session['stressLevel'] = request.POST.get('stressLevel')
                    return render(request, 'mood_getter.html')
                else:
                    # Create and save the SteppingStone instance
                    stepping_stone = SteppingStone(
                        patient=patient,
                        stress_level=request.session['stressLevel'],
                        mood_level=request.session['mood'],
                        personal=request.session['personal'],
                        social=request.session['social'],
                        sleep=request.session['sleep'],
                        actions=request.session['actions'],
                        food=request.session['food'],
                        # Add other fields as needed (score, keywords, emotions)
                    )
                    try:
                        stepping_stone.full_clean()
                        stepping_stone.save()
                        # Clear the session data after saving
                        del request.session['stressLevel']
                        del request.session['mood']
                        del request.session['copingStrategies']
                        del request.session['keywords']
                        del request.session['personal']
                        del request.session['social']
                        del request.session['sleep']
                        del request.session['actions']
                        del request.session['food']
                    except ValidationError as e:
                        # Handle validation errors if needed
                        print(e)
                    return render(request, 'stressLevel.html')
            elif request.method == "GET":
                if request.session.get('food') is not None:
                    return HttpResponse("saves the data and shows emoticard")
                elif request.session.get('actions') is not None:
                    return render(request, 'food.html')
                elif request.session.get('sleep') is not None:
                    return render(request, 'actions.html')
                elif request.session.get('social') is not None:
                    return render(request, 'sleep.html')
                elif request.session.get('personal') is not None:
                    return render(request, 'social.html')
                elif request.session.get('keywords') is not None:
                    print(request.session.get('personal'))
                    return render(request, 'personal.html')
                elif request.session.get('mood') is not None:
                    return render(request, 'keywords.html')
                elif request.session.get('stressLevel') is not None:
                    return render(request, 'mood_getter.html')

                else:
                    request.session['stressLevel'] = None
                    request.session['mood'] = None
                    request.session['keywords'] = None
                    request.session['personal'] = None
                    request.session['social'] = None
                    request.session['sleep'] = None
                    request.session['actions'] = None
                    request.session['food'] = None

                    return render(request, 'stressLevel.html')
    else:
        return redirect('landing')
