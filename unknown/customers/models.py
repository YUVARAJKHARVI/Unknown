from django.db import models
from masters.models import BaseModel

# Create your models here.
class CustomerProfile(BaseModel):
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    profile=models.ImageField(upload_to='customer_profile/%y/%m/%d/',blank=True,null=True)


class EventOrders(BaseModel):
    ORDER_STATUS_CHOICES = ((1, 'Requested'),(2, 'Accepted'),(3, 'Rejected'))
    event=models.ForeignKey('events.EventDetails',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    description = models.CharField(max_length=500)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES,default=0)
    status_notes = models.CharField(max_length=500,blank=True,null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class wishlist(BaseModel):
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    event = models.ForeignKey('events.EventDetails',on_delete=models.CASCADE)
    
