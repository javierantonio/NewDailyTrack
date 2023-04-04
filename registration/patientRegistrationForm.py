from django.contrib.auth.models import User
from .models import Profile, Patient


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
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()

        # Create a new profile
        profile = Profile.objects.create(user=user, email=email, type=usertype, securityQuestion=security_question,
                                         securityAnswer=security_answer, sex=sex, birthday=birthday,
                                         phone=contact_number, address=address)
        profile.save()

        # Create a new patient
        if usertype == 'Patient':
            patient, _ = Patient.objects.get_or_create(profile=profile)
            patient.save()

        return True
