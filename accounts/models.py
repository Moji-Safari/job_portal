import uuid
from django.db import models

class Positions:

    def upload_position_img(instance,filename):
        return f'positions/{instance.id}/{filename}'
    
    img = models.ImageField(upload_to=upload_position_img)
    title=models.CharField(max_length=50,blank=False)
    catagory = models.CharField(max_length=30,choices=CatagoryChoices.choices)
    needed_workforce = models.PositiveIntegerField()
    met_workforce = models.PositiveIntegerField()

    @property
    def remained(self):
        return self.needed_workforce - self.met_workforce

class Skills:
    title = models.TextField(max_length=50)
    related = models.TextChoices()
    experience = models.IntegerField(balnk=False)
    


class EmployeeProfile:
    pic = models.ImageField()
    name = models.TextField(max_length=50)
    education = models.TextChoices()
    profession_catagory = models.TextChoices()
    skill=models.OneToOneField(Skills,on_delete=models.CASCADE,related_name='skill')
    applied_positions=models.IntegerField()
    accepted = models.IntegerField()
    rejected = models.IntegerField()
    



class Employee:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField(EmployeeProfile,on_delete=models.CASCADE,related_name='profile')
    jobs = models.ForeignKey(Positions,on_delete=models.CASCADE)
    
#should be checked
class Application(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)

    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices
    )
    

