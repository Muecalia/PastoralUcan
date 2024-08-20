from rest_framework import serializers
from .models import PastoralGroup
from utils import code_error, message_error
from django.utils import timezone, dateparse
from datetime import datetime as dt

class SavePastoralGroupSerializer(serializers.ModelSerializer):
    #county = serializers.IntegerField(write_only=True)
    foundation_date = serializers.CharField(write_only=True)
    
    class Meta:
        model = PastoralGroup
        fields = '__all__'
        read_only_fields = ('created_date','updated_date')
                
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()        
        if len(attrs['name']) <= 0:
            raise serializers.ValidationError(error_message.error_size(attrs['name']))
        if PastoralGroup.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError(error_message.exists(attrs['name']))
        if (len(attrs['foundation_date']) > 0) &  (not dateparse.parse_datetime(attrs['foundation_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fundação'))
        
        return super().validate(attrs)

    def create(self, validated_data):       

        data = {
            'name': validated_data['name'],
            'description': validated_data['description'],
            'logo': validated_data['logo'],
            'url': validated_data['url'],
            #'foundation_date': dt.fromisoformat(validated_data['foundation_date'])
            'foundation_date': dateparse.parse_datetime(validated_data['foundation_date'])
        }
        
        agreement = PastoralGroup.objects.create(**data)
        return agreement


class ListPastoralGroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = PastoralGroup
        fields = ('id', 'name','url','foundation_date','created_date','logo')
        

class FindPastoralGroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = PastoralGroup
        fields = '__all__'
        

class UpdatePastoralGroupSerializer(serializers.ModelSerializer):
    foundation_date = serializers.CharField(write_only=True)
    
    class Meta:
        model = PastoralGroup
        fields = '__all__'
        read_only_fields = ('created_date','updated_date')
        
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['name']) <= 0:
            raise serializers.ValidationError(error_message.error_size(attrs['name']))
        if (len(attrs['foundation_date']) > 0) &  (not dateparse.parse_datetime(attrs['foundation_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fundação'))
        
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
            
        instance.name = validated_data.get('name', instance.name)
        instance.abbreviation = validated_data.get('abbreviation', instance.abbreviation)
        instance.description = validated_data.get('description', instance.description)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.url = validated_data.get('url', instance.url)
        #instance.foundation_date = validated_data.get(dateparse.parse_datetime(validated_data['foundation_date']), instance.foundation_date)
        instance.foundation_date = dateparse.parse_datetime(validated_data['foundation_date'])
        #instance.foundation_date = dt.fromisoformat(validated_data['foundation_date'])
        instance.updated_date = timezone.now()
        #instance.updated_date = calendar.timegm(time.gmtime()) 
        
        instance.save()
    
        return instance

