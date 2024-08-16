from django.db import models
from django.utils import timezone
from pastoral_activity_api.models import PastoralActivity
from pastoral_coordination_api.models import PastoralCoordination, PastoralMember
from pastoral_visitor_api.models import PastoralVisitor
from enum import Enum


# Create your models here.

class StatusEnum(Enum):
    CANCELADO = 'C'
    PENDENTE = 'P'
    PAGAMENTO_PARCIAL = 'PP'
    PAGAMENTO_TOTAL = 'PT'

class PastoralActivityMember(models.Model):
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now, auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    cancellation_date = models.DateTimeField(null=True, blank=True)
    status_activity = models.CharField(max_length=2, default=StatusEnum.PENDENTE.value)
    pastoral_activity = models.ForeignKey(PastoralActivity, on_delete=models.CASCADE)
    payment = models.FloatField(default=0)
    pastoral_coordination = models.ForeignKey(PastoralCoordination, on_delete=models.CASCADE, blank=True, null=True)
    pastoral_member = models.ForeignKey(PastoralMember, on_delete=models.CASCADE, blank=True, null=True)
    pastoral_visitor = models.ForeignKey(PastoralVisitor, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'tb_pastoral_activity_member'
