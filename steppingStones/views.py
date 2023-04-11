from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from registration.models import Profile, Patient
from steppingStones.models import SteppingStone, Keyword

# Create your views here.

wordValue = []
word = []
wordCategory = []
keywordsToPush = []


def steppingStoneStart(request):
    if request.user.is_authenticated:
        userProfile = Profile.objects.get(user=request.user)
        if userProfile.type == "Patient":
            patient = Patient.objects.get(profile=userProfile)
            if request.method == "POST":
                if request.session['food'] is None and request.session['actions'] is not None:
                    request.session['food'] = int(request.POST.get('food').split('-')[0])
                    request.session['foodDesc'] = request.POST.get('food').split('-')[1]
                    # Processing of keywords
                    anger = 0
                    anticipation = 0
                    joy = 0
                    trust = 0
                    fear = 0
                    surprise = 0
                    sadness = 0
                    disgust = 0
                    score = 0
                    for i in range(len(word)):
                        if wordCategory[i] == 'Anger':
                            anger += int(wordValue[i])
                        elif wordCategory[i] == 'Anticipation':
                            anticipation += int(wordValue[i])
                        elif wordCategory[i] == 'Joy':
                            joy += int(wordValue[i])
                        elif wordCategory[i] == 'Trust':
                            trust += int(wordValue[i])
                        elif wordCategory[i] == 'Fear':
                            fear += int(wordValue[i])
                        elif wordCategory[i] == 'Surprise':
                            surprise += int(wordValue[i])
                        elif wordCategory[i] == 'Sadness':
                            sadness += int(wordValue[i])
                        elif wordCategory[i] == 'Disgust':
                            disgust += int(wordValue[i])
                        score += int(wordValue[i])

                    anger = (anger/score)*100
                    anticipation = (anticipation/score)*100
                    joy = (joy/score)*100
                    trust = (trust/score)*100
                    fear = (fear/score)*100
                    surprise = (surprise/score)*100
                    sadness = (sadness/score)*100
                    disgust = (disgust/score)*100

                    # Create and save the SteppingStone instance
                    import uuid
                    uuid = uuid.uuid4()
                    steppingStone = SteppingStone(
                        patient=patient,
                        # mood and stress level
                        stresslevel=request.session['stressLevel'],
                        moodLevel=request.session['mood'],
                        uuid=uuid,
                        # coping strategies
                        personal=request.session['personal'],
                        personalDesc=request.session['personalDesc'],
                        social=request.session['social'],
                        socialDesc=request.session['socialDesc'],
                        sleep=request.session['sleep'],
                        sleepDesc=request.session['sleepDesc'],
                        actions=request.session['actions'],
                        actionsDesc=request.session['actionsDesc'],
                        food=request.session['food'],
                        foodDesc=request.session['foodDesc'],
                        # keywords
                        anger=anger,
                        anticipation=anticipation,
                        joy=joy,
                        trust=trust,
                        fear=fear,
                        surprise=surprise,
                        sadness=sadness,
                        disgust=disgust,
                        keywords=word,
                    )
                    steppingStone.save()
                    keywordArray = []
                    for i in range(len(word)):
                        keyword = Keyword(
                            uuid=uuid,
                            wordValue=wordValue[i],
                            word=word[i],
                            wordCategory=wordCategory[i]
                        )
                        keywordArray.append(keyword)
                    Keyword.objects.bulk_create(keywordArray)

                    # get all keywords
                    keywords = Keyword.objects.filter(uuid=uuid)
                    # get all stepping stones
                    steppingStones = SteppingStone.objects.get(uuid=uuid)


                    context = {
                        'keywords': keywords,
                        'steppingStones': steppingStones,
                    }
                    request.session['stressLevel'] = None
                    request.session['mood'] = None
                    request.session['keywords'] = None
                    request.session['personal'] = None
                    request.session['social'] = None
                    request.session['sleep'] = None
                    request.session['actions'] = None
                    request.session['food'] = None

                    print (steppingStones.personalDesc)
                    return render(request, 'emoticard.html', context)
                elif request.session['actions'] is None and request.session['sleep'] is not None:
                    request.session['actions'] = int(request.POST.get('actions').split('-')[0])
                    request.session['actionsDesc'] = request.POST.get('actions').split('-')[1]
                    return render(request, 'food.html')
                elif request.session['sleep'] is None and request.session['social'] is not None:
                    request.session['sleep'] = int(request.POST.get('sleep').split('-')[0])
                    request.session['sleepDesc'] = request.POST.get('sleep').split('-')[1]
                    return render(request, 'actions.html')
                elif request.session['social'] is None and request.session['personal'] is not None:
                    request.session['social'] = int(request.POST.get('social').split('-')[0])
                    request.session['socialDesc'] = request.POST.get('social').split('-')[1]
                    return render(request, 'sleep.html')
                elif request.session['personal'] is None and request.session['keywords'] is not None:
                    request.session['personal'] = int(request.POST.get('personal').split('-')[0])
                    request.session['personalDesc'] = request.POST.get('personal').split('-')[1]
                    return render(request, 'social.html')
                elif request.session['keywords'] is None and request.session['mood'] is not None:
                    request.session['keywords'] = request.POST.getlist('keywords')
                    for i in range(len(request.session['keywords'])):
                        wordValue.append(request.session['keywords'][i].split('-')[0])
                        word.append(request.session['keywords'][i].split('-')[1])
                        wordCategory.append(request.session['keywords'][i].split('-')[2])
                    return render(request, 'personal.html')
                elif request.session['mood'] is None and request.session['stressLevel'] is not None:
                    request.session['mood'] = int(request.POST.get('mood').split('-')[0])
                    return render(request, 'keywords.html')
                elif request.session['stressLevel'] is None:
                    request.session['stressLevel'] = request.POST.get('stressLevel')
                    return render(request, 'mood_getter.html')
                else:
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
