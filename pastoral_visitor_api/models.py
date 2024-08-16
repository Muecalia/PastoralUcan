from django.db import models
from django.utils import timezone

# Create your models here.
class PastoralVisitor(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now, auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    state = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'tb_pastoral_visitor'
        ordering = ['name']
        