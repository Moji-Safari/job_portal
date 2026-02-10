from django.db import models
from accounts.models import Employee
from user.models import CategoryChoices


class ApplicationStatus(models.IntegerChoices):
    PENDING = 1, "Pending"
    ACCEPTED = 2, "Accepted"
    REJECTED = 3, "Rejected"


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

class Application(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=ApplicationStatus.choices,default=ApplicationStatus.PENDING
    )


