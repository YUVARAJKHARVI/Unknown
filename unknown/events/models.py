from django.db import models
from masters.models import BaseModel

# Create your models here.
class UserEventDetails(BaseModel):
    event=models.ForeignKey('events.EventDetails',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    description = models.CharField(max_length=500)

class EventDetails(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10)
    
