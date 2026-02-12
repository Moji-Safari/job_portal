from rest_framework import serializers
from . import models

class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeProfile
        fields = ['pic',
                  'name',
                  'education',
                  'profession_catagory',
                  'skill',
                  'bio',
                  'accepted',
                  'rejected']

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployerProfile
        fields = ['pic','name','field','bio','company']
