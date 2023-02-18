from django.db import models
from django.contrib.auth.models import User, Group
import datetime


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
