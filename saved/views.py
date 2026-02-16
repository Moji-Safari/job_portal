from django.shortcuts import render
from rest_framework.views import APIView
from models import Saved
from saved.serializers import SavedSerializer
from rest_framework.response import Response
from accounts.models import Employee
class SavedList(APIView):

    def get(self,request):
        if Employee.is_verified == True:
            queryset = Saved.objects.all()
            serializer = SavedSerializer(queryset,many = True)
            return Response(serializer.data)
        else:
            return Response('please verify your account')


