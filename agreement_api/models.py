from django.db import models
from django.utils import timezone
from institution_api.models import Institution

# Create your models here.
class Agreement(models.Model):
    #name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=500, default='NA', blank=False, null=False)
    state = models.BooleanField(default=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_agreement'
