# serializers.py
from rest_framework import serializers

from registration import google
from .patientRegistrationForm import registerSocialPatientUser

class GoogleAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validateAuthToken(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError('The token is invalid or expired. Please login again.')
        
        # if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
            # raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        given_name = user_data['given_name']
        family_name = user_data['family_name']
        provider = 'google'

        #Redirect to the patientRegistrationForm to create patient account
        return registerSocialPatientUser(
            provider = provider, user_id = user_id, email = email, given_name = given_name, family_name = family_name
        )
