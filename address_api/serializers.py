from rest_framework import serializers
from .models import Country, County, Province


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'



class ProvinceSerializer(serializers.ModelSerializer):
    #country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='description')
    
    class Meta:
        model = Province
        fields = '__all__'
        


class CountySerializer(serializers.ModelSerializer):
    #province = serializers.SlugRelatedField(queryset=Province.objects.all(), slug_field='description')
    
    class Meta:
        model = County
        fields = '__all__'

