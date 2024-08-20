
from enum import Enum


class CivilStateEnum(Enum):
    SOLTEIRO = 'S'
    CASADO = 'C'
    DIVORCIADO = 'D'
    VIUVO = 'V'


class GenderEnum(Enum):
    FEMININO = 'F'
    MASCULINO = 'M'
    OUTRO = 'O'


class Settings:
    
    def get_CivilState(self, state: str):
        list = ('Casado (a)', 'Solteiro', 'Divorciado (a)', 'Viúvo (a)')
        