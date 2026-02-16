from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from models import EmployeeProfile
from serializers import EmployeeProfileSerializer,UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProfileDetail(APIView):
    def get(self,request,id):
        query = EmployeeProfile.objects.get(id=id)
        serializer = EmployeeProfileSerializer(query)
        return Response(serializer.data)

    def post(self,request):
        serializer = EmployeeProfileSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')
    
    def patch(self,request,pk):
        query = get_object_or_404(EmployeeProfile, pk=pk)
        serializer = EmployeeProfileSerializer(query,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    

