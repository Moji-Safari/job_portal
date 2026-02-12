from django.db import models
from stake.models import Positions

class Saved(models.Model):
    saved_position = models.ForeignKey(Positions,on_delete=models.CASCADE,)
    saved_date = models.DateField(auto_now_add=True)
    #reminder = models.DateField() *** will be added.
