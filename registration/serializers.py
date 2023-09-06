# serializers.py
from rest_framework import serializers
from .models import *

class GoogleAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    
