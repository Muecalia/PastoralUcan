from rest_framework import serializers
from .models import Congregation, Religion, Sacrament



class CongregationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Congregation
        fields = '__all__'
        #read_only_fields = ('id')    



class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = '__all__'



class SacramentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Sacrament
        fields = '__all__'

