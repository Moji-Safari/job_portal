from django.shortcuts import render
from rest_framework.views import APIView
from models import Saved
from saved.serializers import SavedJobSerializer
from rest_framework.response import Response
from accounts.models import Employee,User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class SavedList(APIView):

    def get(self,request):
        if Employee.is_verified == True:
            queryset = Saved.objects.all()
            serializer = SavedJobSerializer(queryset,many = True)
            return Response(serializer.data)
        else:
            return Response('please verify your account')

class SaveToDashboard(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
            data = request.data.copy()
            data['user']=request.user.id
            serializer = SavedJobSerializer(data = data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data,status=status.HTTP_201_CREATED)
            
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        





