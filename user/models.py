from django.db import models


class CategoryChoices(models.TextChoices):
    HEALTH="health","health"
    TECH="tech","tech"
    ENGINEERING="eng","engineering"
    FINANCE="finance","financial"
    ENTERTAINMENT="entertnmt","entertainment"


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
