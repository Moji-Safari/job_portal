from rest_framework import serializers
from models import User,Employee,Employer,EmployeeProfile,EmployerProfile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields=['email','username','password']

        def create(self,validated_data):
            user = User.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password']
            )
            return user

        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['profile']


class EmployerSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['emplyr_pro','offered','emplr_acc','emplr_rjct']

class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
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
        model = EmployerProfile
        fields = ['pic','name','field','bio','company']

