from . import models
from rest_framework import serializers
from models import Saved


class SavedJobSerializer(serializers.Serializer):
    class Meta:
        model = Saved
        fields=['saved_position','saved_date']