from django.db import models
from masters.models import BaseModel

# Create your models here.
class VendorProfile(BaseModel):
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    shop_latitude = models.FloatField()
    shop_longitude = models.FloatField()
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    verified_note = models.CharField(max_length=100, blank=True, null=True)
    documents = models.JSONField(default=dict)
    profile=models.ImageField(upload_to='vendor_profile/%y/%m/%d/',blank=True,null=True)


class EventDetails(BaseModel):
    vendor=models.foreignkey('vendors.VendorDetails',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10)
    files=models.JSONField(default=list)
    #single location for perticular events
    latitude = models.FloatField()
    longitude = models.FloatField()


class Pricing(BaseModel):
    PAYMENT_STATUS_CHOICES = ((1, 'Pending'),(2, 'Completed'),(3, 'Cancelled'))
    vendor=models.ForeignKey('vendors.VendorDetails',on_delete=models.CASCADE)
    fees=models.DecimalField(max_digits=10)
    discount=models.DecimalField(max_digits=10)
    payment_method=models.CharField(max_length=100)
    payment_gateway=models.CharField(max_length=100)
    payment_status=models.IntegerField(_("payment status"),default=0,choices=PAYMENT_STATUS_CHOICES)
    payment_status_notes=models.CharField(max_length=100,blank=True,null=True)
    payment_datetime=models.DateTimeField()
    payment_id=models.CharField(max_length=100,blank=True,null=True)
