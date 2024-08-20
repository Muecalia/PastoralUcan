from django.db import models
from address_api.models import Country, County
#from datetime import datetime as dt
from django.utils import timezone

# Create your models here.
class TypeInstitution(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    #created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    #created_date = models.DateTimeField(default=dt.now)
    #update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "tb_type_institution"
        ordering = ['name']


class Institution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    phone = models.CharField(max_length=20, blank=False, null=False, unique=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    state = models.BooleanField(default=True)
    type = models.ForeignKey(TypeInstitution, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    updated_date = models.DateTimeField(null=True)
    
    class Meta:
        db_table = 'tb_institution'
        ordering = ['name']
