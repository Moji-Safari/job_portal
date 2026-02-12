
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from serializers import PositionSerializer
from models import Positions

class JobsList(APIView):
    def get(self,request):
        jobs = Positions.objects.all()
        serializer = PositionSerializer(jobs,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PositionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')



