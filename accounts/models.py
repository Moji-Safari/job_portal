import uuid
from django.db import models
class ApplicationStatus(models.IntegerChoices):
    PENDING = 1, "Pending"
    ACCEPTED = 2, "Accepted"
    REJECTED = 3, "Rejected"

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
    
    


class Positions(models.Model):

    def upload_position_img(instance,filename):
        return f'positions/{instance.id}/{filename}'
    
    img = models.ImageField(upload_to=upload_position_img)
    title=models.CharField(max_length=50,blank=False)
    category = models.CharField(max_length=30,choices=CategoryChoices.choices)
    needed_workforce = models.PositiveIntegerField()
    met_workforce = models.PositiveIntegerField()

    @property
    def remained(self):
        return self.needed_workforce - self.met_workforce


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField(EmployeeProfile,on_delete=models.CASCADE,related_name='profile')
    #jobs = models.ManyToManyField(Positions,)

class EmployerProfile(models.Model):
    def upload_position_img(instance,filename):
        return f'EmployerProfile/{instance.id}/{filename}'
    pic = models.ImageField()
    name = models.CharField(max_length=30)
    field = models.CharField(max_length=50,choices=CategoryChoices.choices)
    bio = models.TextField()
    company = models.CharField(max_length=30)
    email = models.EmailField()




class Employer(models.Model):
    emplyr_pro = models.OneToOneField(EmployerProfile,on_delete=models.CASCADE)
    offered = models.CharField(max_length=50)
    



#should be checked
class Application(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=ApplicationStatus.choices,default=ApplicationStatus.PENDING
    )


