from django.db import models
from django.utils import timezone
from general_api.models import TypeActivity
from enum import Enum

class StatusEnum(Enum):
    CREATED = 'C'
    SUSPENDED = 'S'
    PUBLISHED = 'P'
    

# Create your models here.
class PastoralActivity(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(blank=False, null=False)
    publication_date = models.DateTimeField(blank=True, null=True)
    suspended_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    status = models.CharField(max_length=2, default=StatusEnum.CREATED.value)
    type_activity = models.ForeignKey(TypeActivity, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tb_pastoral_activity'
        ordering = ['name']



