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
        # password = request.POST['password']
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
        userData.first_name = first_name
        userData.last_name = last_name 
        # userData.password = password  
        userData.email = email    
        userData.save()   

        # Update Profile
        profileData.sex = sex
        profileData.birthday = birthday
        profileData.phone = contact_number
        profileData.address = address            
        # profileData.securityAnswer = security_answer
        # profileData.securityQuestion = security_question
              
        profileData.save()

        #Update Specialist
        specialistData.licenseExpiry = license_expiry
        specialistData.licenseNumber = license_number
        # specialistData.prcID = prc_id
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
        # password = request.POST['password']
        # security_question = request.POST['securityQuestion']
        # security_answer = request.POST['securityAnswer']
        # Personal Details
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        contact_number = request.POST['contactNumber']
        address = request.POST['address']
        # Patient Details
        # guardian_email = request.POST['guardianEmail']


        # Update User
        userData.first_name = first_name
        userData.last_name = last_name 
        # userData.password = password   
        userData.email = email
        userData.save()

        # Update Profile
        profileData.sex = sex
        profileData.birthday = birthday
        profileData.phone = contact_number
        profileData.address = address            
        # profileData.securityAnswer = security_answer
        # profileData.securityQuestion = security_question               
        profileData.save()

        #Update Patient
        # patientData.guardianEmail = guardian_email
        patientData.save()

        print ("Patient Profile updated")

        return True
