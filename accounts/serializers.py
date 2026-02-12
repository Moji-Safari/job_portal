from rest_framework import serializers
from . import models

        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['profile']


class EmployerSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = models.Employer
        fields = ['emplyr_pro','offered','emplr_acc','emplr_rjct']

