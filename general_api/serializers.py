from rest_framework import serializers
from .models import AcademicLevel, TypeActivity, University, School


class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = '__all__'


class TypeActivitySerializer(serializers.ModelSerializer):    
    class Meta:
        model = TypeActivity
        fields = '__all__'
        

class UniversitySerializer(serializers.ModelSerializer):    
    class Meta:
        model = University
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):    
    class Meta:
        model = School
        fields = '__all__'
        
        
