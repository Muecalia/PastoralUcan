from django.db import models
from datetime import datetime as dt
from django.utils import timezone
from institution_api.models import Institution

# Create your models here.

class Provider(models.Model):
    nif = models.CharField(max_length=20, null=False, blank=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    #created_date = models.DateTimeField(default=dt.now)
    update_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_provider'
        ordering = ['created_date']
