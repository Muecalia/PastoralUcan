from django.db import models

# Create your models here.
class AcademicLevel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'tb_academic_level'


class TypeActivity(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'tb_type_activity'


class University(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    abbreviation = models.CharField(max_length=5)

    class Meta:
        db_table = 'tb_university'

        
class School(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    abbreviation = models.CharField(max_length=5)

    class Meta:
        db_table = 'tb_school'
        

