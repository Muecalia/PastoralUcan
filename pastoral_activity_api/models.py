from django.db import models
from django.utils import timezone
from general_api.models import TypeActivity


# Create your models here.
class PastoralActivity(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now, auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    state = models.BooleanField(default=True)
    type_activity = models.ForeignKey(TypeActivity, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tb_pastoral_activity'
        ordering = ['name']



