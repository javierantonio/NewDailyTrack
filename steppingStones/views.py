from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

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
                    return HttpResponse('Move to food.')

                elif request.session['sleep'] is None and request.session['social'] is not None:
                    request.session['sleep'] = request.POST.get('sleep')
                    return HttpResponse('Move to actions.')

                elif request.session['social'] is None and request.session['personal'] is not None:
                    request.session['social'] = request.POST.get('social')
                    return HttpResponse('Move to sleep.')

                elif request.session['personal'] is None and request.session['keywords'] is not None:
                    request.session['personal'] = request.POST.get('personal')
                    return HttpResponse('Move to social.')

                elif request.session['keywords'] is None and request.session['mood'] is not None:
                    request.session['keywords'] = request.POST.get('keywords')
                    return HttpResponse('Move to personal.')

                elif request.session['mood'] is None and request.session['stressLevel'] is not None:
                    request.session['mood'] = request.POST.get('mood')
                    return HttpResponse('Move to keywords.')

                elif request.session['stressLevel'] is None:
                    request.session['stressLevel'] = request.POST.get('stressLevel')
                    return HttpResponse('Move to mood.')

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
                    return render(request, 'distress_scale.html')

            elif request.method == "GET":
                if request.session.get('keywords') is not None:
                    return HttpResponse("this go to the personal page")
                elif request.session.get('mood') is not None:
                    return HttpResponse("this go to the keywords page")
                elif request.session.get('stressLevel') is not None:
                    return render(request, 'mood_getter.html')
                return render(request, 'distress_scale.html')
    else:
        return redirect('landing')