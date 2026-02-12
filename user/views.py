from rest_framework.response import Response
from rest_framework.views import APIView
from models import EmployeeProfile
from serializers import EmployeeProfileSerializer

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




