from django.db import models
from django.utils import timezone
from agreement_api.models import Agreement
from enum import Enum

# Create your models here.
class StateProjectEnum(Enum):
    Suspended = 1
    Completed = 2
    Progress = 3
    Pending = 4


class AgreementProject(models.Model):
    description_project = models.CharField(max_length=500, null=False, blank=False)
    #state_project = models.BooleanField(default=True)
    #state_project = models.IntegerField(choices=StateProjectEnum, default=StateProjectEnum.Pending)
    state_project = models.IntegerField(default=StateProjectEnum.Pending)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(blank=True, null=True)
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_agreement_project'
        ordering = ['created_date']
