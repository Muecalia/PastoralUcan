from django.db import models

# Create your models here.

class Religion(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    
    class Meta:
        db_table = 'tb_religion'


class Congregation(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = 'tb_congregation'


class Sacrament(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    
    class Meta:
        db_table = 'tb_sacrament'
    