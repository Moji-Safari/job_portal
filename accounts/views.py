from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from models import EmployeeProfile,Employer
from serializers import EmployeeProfileSerializer,UserSerializer,EmployerSerialaizer
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PrivateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated"})


class ProfileDetail(APIView):
    def get(self,request,id):
        query = EmployeeProfile.objects.get(pk=id)
        serializer = EmployeeProfileSerializer(query)
        return Response(serializer.data)

    def post(self,request):
        serializer = EmployeeProfileSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def patch(self,request,pk):
        query = get_object_or_404(EmployeeProfile, pk=pk)
        serializer = EmployeeProfileSerializer(query,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class JobStatusView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            query = Employer.objects.get(id = request.user.id)
            serializer = EmployerSerialaizer(query)
            return Response(serializer.data)
        except Employer.DoesNotExist:
            return Response(
                {'detail':'Employer profile not found'},status=status.HTTP_404_NOT_FOUND)

    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = EmployerSerialaizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    

