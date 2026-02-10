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
        
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Positions
        fields = ['img','title','category','needed_workforce','remained']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['profile']

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employer
        fields = ['pic','name','field','bio','company']

class EmployerSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = models.Employer
        fields = ['emplyr_pro','offered','emplr_acc','emplr_rjct']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields =['employee','position','applied_at','status']        