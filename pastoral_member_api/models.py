from django.db import models
from enum import Enum
from django.utils import timezone
from address_api.models import Country, County
from religion_api.models import Religion, Sacrament
from general_api.models import AcademicLevel, School, University

# Create your models here.
class CivilStateEnum(Enum):
    SOLTEIRO = 'S'
    CASADO = 'C'
    DIVORCIADO = 'D'
    VIUVO = 'V'


class GenderEnum(Enum):
    FEMININO = 'F'
    MASCULINO = 'M'
    OUTRO = 'O'


class PastoralMember(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False, db_index=True)
    last_name = models.CharField(max_length=50, null=False, blank=False, db_index=True)
    photo = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=20, null=False, blank=False)
    birth_date = models.DateTimeField(null=True, blank=True)
    nacionality = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, null=True, blank=True)
    sacrament = models.ForeignKey(Sacrament, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length = 1, null=True, blank=True)
    civil_state = models.CharField(max_length = 1, default=CivilStateEnum.SOLTEIRO.value)
    academic_level = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True, blank=True)
    state = models.BooleanField(default=False)
    street = models.CharField(max_length=30, null=True, blank=True)
    house_number = models.CharField(max_length=10, null=True, blank=True)
    #groups = models.ManyToManyField(PastoralGroup, through='PastoralMemberHasGroup')
    created_date = models.DateTimeField(default=timezone.now(), auto_created=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_pastoral_member'
        ordering = ('last_name', 'first_name')
    
