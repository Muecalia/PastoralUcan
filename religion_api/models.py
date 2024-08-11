from django.db import models

# Create your models here.
class Congregation(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    
    class Meta:
        db_table = 'tb_congregation'


class Religion(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    
    class Meta:
        db_table = 'tb_religion'



class Sacrament(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    
    class Meta:
        db_table = 'tb_sacrament'
    