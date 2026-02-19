import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from stake.models import Application,Positions

class User(AbstractUser):
    email = models.EmailField(unique=True)
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
   


class CategoryChoices(models.TextChoices):
    HEALTH="health","Health"
    TECH="tech","Tech"
    ENGINEERING="eng","Engineering"
    FINANCE="finance","Financial"
    ENTERTAINMENT="entertnmt","Entertainment"


class Degree(models.IntegerChoices):
    NODEG = 1, "No degree"
    bach = 2, "Bachelore"
    mast = 3, "Master"
    doc = 4,"PHD"

class Skills(models.Model):
    title = models.CharField(max_length=50)
    related = models.CharField(choices=CategoryChoices.choices)
    experience = models.IntegerField()
    

class EmployeeProfile(models.Model):
    pic = models.ImageField()
    name = models.CharField(max_length=50)
    education = models.CharField(choices=Degree.choices)
    profession_catagory = models.TextChoices()
    skill=models.ManyToManyField(Skills,related_name='employee')
    bio = models.TextField()
    applied_positions=models.CharField(max_length=50)
    email = models.EmailField()
    accepted = models.PositiveIntegerField(default=0)
    rejected = models.PositiveIntegerField(default=0)
    
    
class EmployerProfile(models.Model):
    def upload_position_img(instance,filename):
        return f'EmployerProfile/{instance.id}/{filename}'
    pic = models.ImageField()
    name = models.CharField(max_length=30)
    field = models.CharField(max_length=50,choices=CategoryChoices.choices)
    bio = models.TextField()
    company = models.CharField(max_length=30)
    email = models.EmailField()

    


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField(EmployeeProfile,on_delete=models.CASCADE,related_name='profile')
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    #jobs = models.ManyToManyField(Positions,)



class Employer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    emplyr_pro = models.OneToOneField(EmployerProfile,on_delete=models.CASCADE)
    offered = models.ForeignKey(Positions,on_delete=models.CASCADE,related_name='offered')
    emplr_acc = models.ForeignKey(Application,on_delete=models.CASCADE,related_name='accepted')
    emplr_rjct = models.ForeignKey(Application,on_delete=models.CASCADE,related_name='rejected')



