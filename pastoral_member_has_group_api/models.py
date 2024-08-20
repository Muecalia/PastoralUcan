from django.db import models
from django.utils import timezone
from pastoral_group_api.models import PastoralGroup
from pastoral_member_api.models import PastoralMember

# Create your models here.
class PastoralMemberHasGroup(models.Model):
    pastoral_member = models.ForeignKey(PastoralMember, on_delete=models.CASCADE)
    pastoral_group = models.ForeignKey(PastoralGroup, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_pastoral_member_has_group'

        