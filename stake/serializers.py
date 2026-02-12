from rest_framework import serializers
from models import Positions,Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields =['employee','position','applied_at','status']        

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ['img','title','category','needed_workforce','remained']
               