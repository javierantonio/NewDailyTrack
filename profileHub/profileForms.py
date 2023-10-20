from django.contrib.auth.models import User
from datetime import datetime
from registration.models import Profile, Patient, Specialist

def specialistUpdate(request):
    userData = Profile.objects.get(user=request.user).user
    profileData = Profile.objects.get(user=request.user)
    specialistData = Specialist.objects.get(profile=profileData)

    if request.method == 'POST':
        # Auth Details
        email = request.POST['email']
        # security_question = request.POST['securityQuestion']
        # security_answer = request.POST['securityAnswer']
        # Personal Details
        #(datetime.strptime(request.POST['birthday'],'%m/%d/%Y')).strftime('%Y-%m-%d')
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        contact_number = request.POST['contactNumber']
        address = request.POST['contactNumber']
        
        # Professional Details
        # prc_id = request.POST['prcID']
        license_number = request.POST['licenseNumber']
        license_expiry = request.POST['licenseExpiry']

        # Update User
        userData.username = email
        userData.first_name = first_name
        userData.last_name = last_name 
        userData.email = email   
        # profileData.securityAnswer = security_answer
        # profileData.securityQuestion = security_question 

        # Update Profile
        profileData.email = email
        profileData.sex = sex
        profileData.birthday = birthday
        profileData.phone = contact_number
        profileData.address = address        

        #Update Specialist
        specialistData.licenseExpiry = license_expiry
        specialistData.licenseNumber = license_number
        # specialistData.prcID = prc_id

        editProfileForm = request.POST

        if 'password' in editProfileForm:
            userData.set_password(editProfileForm['password']) 

        userData.save() 
        profileData.save()
        specialistData.save()

        print ("Specialist Profile updated")

        return True

def patientUpdate(request):
    userData = Profile.objects.get(user=request.user).user
    profileData = Profile.objects.get(user=request.user)
    patientData = Patient.objects.get(profile=profileData)

    if request.method == 'POST':
        # Auth Details
        email = request.POST['email']
        # security_question = request.POST['securityQuestion']
        # security_answer = request.POST['securityAnswer']

        # Personal Details
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        contact_number = request.POST['contactNumber']
        address = request.POST['address']

        # Update User
        userData.username = email
        userData.first_name = first_name
        userData.last_name = last_name 
        userData.email = email

        # Update Profile
        profileData.email = email
        profileData.sex = sex
        profileData.birthday = birthday
        profileData.phone = contact_number
        profileData.address = address            
        # profileData.securityAnswer = security_answer
        # profileData.securityQuestion = security_question 

        editProfileForm = request.POST

        if 'password' in editProfileForm:
            userData.set_password(editProfileForm['password']) 

        if 'guardianEmail' in editProfileForm:
            patientData.guardianEmail = editProfileForm['guardianEmail']
            patientData.save()

        userData.save() 
        profileData.save()

        print ("Patient Profile updated")

        return True
