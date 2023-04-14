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

                    anger = (anger / score) * 100
                    anticipation = (anticipation / score) * 100
                    joy = (joy / score) * 100
                    trust = (trust / score) * 100
                    fear = (fear / score) * 100
                    surprise = (surprise / score) * 100
                    sadness = (sadness / score) * 100
                    disgust = (disgust / score) * 100

                    copingStrategyScore = request.session['personal'] + request.session['social'] + request.session[
                        'sleep'] + request.session['actions'] + request.session['food']
                    copingStrategyName = None
                    copingStrategyDesc = None

                    emotions = {
                        'Anger': anger,
                        'Anticipation': anticipation,
                        'Joy': joy,
                        'Trust': trust,
                        'Fear': fear,
                        'Surprise': surprise,
                        'Sadness': sadness,
                        'Disgust': disgust
                    }
                    feelingDesc = None
                    feelingValue = max(emotions.values())
                    feelingName = max(emotions, key=emotions.get)
                    if feelingName == "Anger":
                        feelingDesc = "You want to attack an obstacle that is getting in the way of your peace."
                    elif feelingName == "Anticipation":
                        feelingDesc = "You are highly focused and alert; on the lookout for something."
                    elif feelingName == "Joy":
                        feelingDesc = "You are delighted! Things are better going good for you and you feel an abundance of energy."
                    elif feelingName == "Trust":
                        feelingDesc = "You feel a deep connection and pride for a person or idea that makes you want to strengthen your commitment to it."
                    elif feelingName == "Fear":
                        feelingDesc = "You sense a big danger, making you alarmed or petrified."
                    elif feelingName == "Surprise":
                        feelingDesc = "You feel inspired by something that caught you off guard. You want to remember that moment."
                    elif feelingName == "Sadness":
                        feelingDesc = "You are in a state of heartbreak and distraught after losing something dear. It feels hard to get up and go on."
                    elif feelingName == "Disgust":
                        feelingDesc = "You feel disturbed, horrified, and violated. You want to block it all out."
                    if copingStrategyScore <= 1:
                        copingStrategyName = "Functional Acceptant"
                        copingStrategyDesc = "You let things come and go appropriately, letting yourself feel emotions but not letting them sit in for too long in your head to the point of it being unhealthy. You actively embrace the subjective experience, particularly your distressing experiences. You understand that the idea is not merely to grudgingly tolerate negative experiences but to embrace them fully and without defense."
                    elif copingStrategyScore <= 20:
                        copingStrategyName = "Mostly Acceptant"
                        copingStrategyDesc = "You recognize that there will be times wherein your mental and emotional fortitude are challenged, but you also recognize that trying to escape from emotional pain will never work. Instead, you let go of attempts to avoid or control your thoughts and feelings to focus more on living a meaningful life."
                    elif copingStrategyScore <= 40:
                        copingStrategyName = "Well-Adjusted"
                        copingStrategyDesc = "While you acknowledge the need to avoid negative stimuli for your own well-being, you cope well enough and continue to function without being self-destructive or self-sabotaging."
                    elif copingStrategyScore <= 60:
                        copingStrategyName = "Mostly Avoidant"
                        copingStrategyDesc = "You try to steer clear of troubling stimuli so that you do not have to confront any negative emotions. You might also be turning to risky behavior to cope and may even withdraw from social experiences to prevent feelings of anxiety."
                    elif copingStrategyScore <= 80:
                        copingStrategyName = "Experiential Avoidant"
                        copingStrategyDesc = "You do everything you can to not come into contact with anything that can trigger unwanted internal experiences, such as emotions, thoughts, memories, and bodily sensations. This may also include damaging forms of coping such as substance abuse, risky sexual behavior, and deliberate self-harm."

                    # Create and save the SteppingStone instance
                    import uuid
                    uuid = uuid.uuid4()
                    steppingStone = SteppingStone(
                        patient=patient,
                        # mood and stress level
                        stressLevel=request.session['stressLevel'],
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
                        # coping strategy score
                        copingStrategyScore=copingStrategyScore,
                        copingStrategyName=copingStrategyName,
                        copingStrategyDesc=copingStrategyDesc,
                        feelingDesc=feelingDesc,
                        feelingValue=feelingValue,
                        feelingName=feelingName,
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
