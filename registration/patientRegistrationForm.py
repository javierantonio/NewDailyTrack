from datetime import datetime, date
import os

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import login

from .models import Profile, Patient
# from .serializers import GoogleAuthSerializer

def processPatientRegistration(request):
    if request.method == 'POST':

        # Get the form data from the request
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        security_question = request.POST['securityQuestion']
        security_answer = request.POST['securityAnswer']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        contact_number = request.POST['contactNumber']
        address = request.POST['address']
        usertype = 'Patient'

        # Create a new user
        user = User.objects.create_user(username=email, 
                                        email=email, 
                                        password=password, 
                                        first_name=first_name,
                                        last_name=last_name)
        user.save()

        # Create a new profile
        profile = Profile.objects.create(user=user, 
                                         email=email, 
                                         type=usertype, 
                                         securityQuestion=security_question,
                                         securityAnswer=security_answer, 
                                         sex=sex, 
                                         birthday=birthday,
                                         phone=contact_number, 
                                         address=address)
        profile.save()

        # patient = Patient.objects.get_or_create(profile=profile)
        patient = Patient.objects.create(profile=profile)
        
        current_date = datetime.now().date()

        if (relativedelta(current_date, datetime.strptime(birthday, '%Y-%m-%d').date())).years < 18:
            subject = 'Guardian Email Confirmation'
            if profile.sex == 'male':
                pronoun = 'his'
            elif profile.sex == 'female':
                pronoun = 'her'
            else:
                pronoun = 'their'
            html_content = render_to_string('guardianEmail.html', {'user': user, 'pronoun': pronoun})
            sender_email = 'dailytrack@dailytrack.online'
            recipient_email = request.POST['guardianEmail']
            print(request.POST['guardianEmail'])
            text_content = strip_tags(html_content)
            print("Sending email...")
            msg = EmailMultiAlternatives(subject, text_content, sender_email, [recipient_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            
            guardian_email = request.POST['guardianEmail']
            patient.guardian_email = guardian_email
            patient.save()

        return True
    
def registerSocialPatientUser(provider, user_id, email, family_name, given_name):
    filter_user_by_email = User.objects.filter(email=email)

    if filter_user_by_email.exists():
        if provider == filter_user_by_email[0].auth_provider:
            #If user already exists, login the user in the system
            registered_user = login.views(email=email,password=os.environ.get('SOCIAL_SECRET'))
        
        return {
            'username': registered_user.email,
            'email': registered_user.email,
            # 'tokens': registered_user.tokens()
        }

    else:
        email = email
        password = os.environ.get('SOCIAL_SECRET')
        first_name = given_name
        last_name = family_name
        security_question = ''
        security_answer = ''
        sex = ''
        birthday = ''
        contact_number = ''
        address = ''
        usertype = 'Patient'

        # Create a new user
        user = User.objects.create_user(username=email, 
                                        email=email, 
                                        password=password, 
                                        first_name=first_name,
                                        last_name=last_name)
        user.save()

        # Create a new profile
        profile = Profile.objects.create(user=user, 
                                         email=email, 
                                         type=usertype, 
                                         securityQuestion=security_question,
                                         securityAnswer=security_answer, 
                                         sex=sex, 
                                         birthday=birthday,
                                         phone=contact_number, 
                                         address=address)
        profile.save()

        return True
