from django.shortcuts import render
from rest_framework.views import APIView
from models import Saved
from saved.serializers import SavedSerializer
from rest_framework.response import Response

class SavedList(APIView):
    def get(self,request):
        queryset = Saved.objects.all()
        serializer = SavedSerializer(queryset,many = True)
        return Response(serializer.data)


