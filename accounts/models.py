import uuid
from django.db import models
from user.models import EmployeeProfile,EmployerProfile


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField(EmployeeProfile,on_delete=models.CASCADE,related_name='profile')
    #jobs = models.ManyToManyField(Positions,)



class Employer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    emplyr_pro = models.OneToOneField(EmployerProfile,on_delete=models.CASCADE)
    offered = models.CharField(max_length=50)
    emplr_acc = models.CharField(max_length=50)
    emplr_rjct = models.CharField(max_length=50)
    

