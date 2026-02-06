from django.db import models

class Positions:
    img = models.ImageField()
    title=models.TextField(max_length=50,blank=False)
    catagory = models.TextChoices()
    needed_workforce = models.IntegerField()
    met_workforce = models.IntegerField()
    remained = models.IntegerField()

class Skills:
    title = models.TextField(max_length=50)
    related = models.TextChoices()
    experience = models.IntegerField(balnk=False)
    


class EmployeeProfile:
    pic = models.ImageField()
    name = models.TextField(max_length=50)
    profession_catagory = models.TextChoices()
    skill=models.OneToOneField(Skills,on_delete=models.CASCADE,related_name='skill')
    applied_positions=models.IntegerField()
    accepted = models.IntegerField()
    rejected = models.IntegerField()



class Employee:
    profile = models.OneToOneField(EmployeeProfile,on_delete=models.CASCADE,related_name='profile')
    

    

