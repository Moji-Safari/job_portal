from rest_framework import serializers
from . import models


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields =['employee','position','applied_at','status']        

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Positions
        fields = ['img','title','category','needed_workforce','remained']
               