from django.contrib.auth.models import User
from .models import Profile, Specialist
from django.core.files.storage import FileSystemStorage

def processSpecialistRegistration(request):

    if request.method == 'POST':
        
        # Get the form data from the request
        email = request.POST['email']
        password = request.POST['password']
        security_question = request.POST['securityQuestion']
        security_answer = request.POST['securityAnswer']
        image_file = request.FILES['image_file']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        contact_number = request.POST['contactNumber']
        address = request.POST['address']
        license_number = request.POST['licenseNumber']
        license_expiry = request.POST['licenseExpiry']
        usertype = 'Specialist'

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
                                         phone=contact_number, 
                                         address=address,
                                         birthday=birthday)
        profile.save()
    

        #Create a new specialist
        specialist = Specialist.objects.create(profile=profile, 
                                               prcID=image_file,
                                               licenseNumber = license_number, 
                                               licenseExpiry = license_expiry)
        specialist.save()

        print ("Specialist Profile created")

        return True
