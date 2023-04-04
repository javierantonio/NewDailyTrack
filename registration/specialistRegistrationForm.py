from django.contrib.auth.models import User
from .models import Profile, Specialist


def processSpecialistRegistration(request):

    if request.method == 'POST':

        # Get the form data from the request
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        security_question = request.POST['securityQuestion']
        security_answer = request.POST['securityAnswer']
        sex = request.POST['sex']
        contact_number = request.POST['contactNumber']
        address = ""
        usertype = 'Specialist'

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()

        # Create a new profile
        profile = Profile.objects.create(user=user, email=email, type=usertype, securityQuestion=security_question,
                                         securityAnswer=security_answer, sex=sex,
                                         phone=contact_number, address=address)
        profile.save()

        # Create a new patient
        if usertype == 'Specialist':
            specialist, _ = Specialist.objects.get_or_create(profile=profile)
            specialist.save()

        return True
