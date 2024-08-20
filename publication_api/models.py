from django.db import models
from django.utils import timezone
from pastoral_activity_api.models import PastoralActivity

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False)
    path_photo = models.CharField(max_length=100, null=True, blank=True)
    pastoral_activity = models.ForeignKey(PastoralActivity, on_delete=models.CASCADE, null=True, blank=True)    
    created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_publication'
        ordering = ["title"]
        