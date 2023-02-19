from django.db import models
from django.contrib.auth.models import User, Group
import datetime
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class BaseModel(models.Model):
    STATUS_CHOICES = ((1, 'Inactive'),(2, 'Active'),(3, 'Deleted'),)

    '''
    BaseModel
    '''
    uuid = models.CharField(editable=False, unique=True, max_length=200)
    server_created_on = models.DateTimeField(auto_now_add=True,verbose_name='created time')
    server_modified_on = models.DateTimeField(auto_now=True,verbose_name='updated time')
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=2, db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', null=True, blank=True,)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', null=True, blank=True,)

    class Meta:
        abstract = True
    
    def create(self, *args, **kwargs):
        curr_dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.uuid = str(uuid.uuid4()) + "-" + str(curr_dt)
        super(BaseContent, self).save(*args, **kwargs)


class Queries(BaseModel):
    QUERY_STATUS_CHOICES = ((1, 'Pending'),(2, 'Solved'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    text=models.CharField(max_length=500)
    solution=models.CharField(max_length=500,blank=True,null=True)
    status = models.IntegerField(choices=QUERY_STATUS_CHOICES,default=0)
    files=models.JSONField(default=list)


class Feedback(BaseModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    text=models.CharField(max_length=500)
    rating = models.IntegerField(default=0)
    files=models.JSONField(default=list)
