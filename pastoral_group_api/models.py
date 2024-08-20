from django.db import models
from django.utils import timezone

# Create your models here.

class PastoralGroup(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    abbreviation = models.CharField(max_length=10, null=True, blank=True, default='NA')
    description = models.CharField(max_length=2000, null=True, blank=True, default='NA')
    logo = models.CharField(max_length=50, null=False, blank=False, default='NA')
    url = models.CharField(max_length=50, null=False, blank=False, default='NA')
    created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    foundation_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_pastoral_group'
        ordering = ['name']
    