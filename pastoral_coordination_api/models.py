from django.db import models
from django.utils import timezone
from pastoral_member_api.models import PastoralMember


# Create your models here.
class PastoralCoordination(models.Model):
    status = models.BooleanField(default=True)
    history = models.TextField(null=True, blank=True)
    profile_id = models.IntegerField(null=False, blank=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(blank=True, null=True)
    pastoral_member = models.ForeignKey(PastoralMember, on_delete=models.CASCADE, null=False)
    created_date = models.DateTimeField(default=timezone.now, auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    renewal_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_pastoral_coordination'
    