from rest_framework import serializers
from .models import County, Institution, TypeInstitution
#from address_api.models import County
from utils import code_error, message_error
from datetime import datetime as dt
from django.utils import timezone

class TypeInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeInstitution
        fields = '__all__'


class ListInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class SaveInstitutionSerializer(serializers.ModelSerializer):
    county = serializers.IntegerField(write_only=True)
    type = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Institution
        fields = ('name', 'email','phone','county','street','type')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()     
        if Institution.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError(error_message.exists('name'))            
        if Institution.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(error_message.exists('email'))        
        if Institution.objects.filter(phone=attrs['phone']).exists():
            raise serializers.ValidationError(error_message.exists('phone'))
        if not County.objects.filter(id=attrs['county']):
            raise serializers.ValidationError(error_message.not_found('County'))
        if not TypeInstitution.objects.filter(id=attrs['type']):
            raise serializers.ValidationError(error_message.not_found('Type Institution'))
        return attrs
        
    def create(self, validated_data):        
        data = {
            'name': validated_data['name'],
            'email': validated_data['email'],
            'phone': validated_data['phone'],
            'county': County.objects.get(id=validated_data['county']),
            'street': validated_data['street'],
            'code': 'NA',
            #'code': validated_data['code'],
            'type': TypeInstitution.objects.get(id=validated_data['type'])
        }
        
        institution = Institution.objects.create(**data)
        
        return institution


class UpdateInstitutionSerializer(serializers.ModelSerializer):
    county = serializers.IntegerField(write_only=True)
    type = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Institution
        fields = ('name', 'email','phone','county','street','type')
    
    '''def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if not County.objects.filter(id=attrs['county']):
            raise serializers.ValidationError(error_message.not_found('County'))
        if not TypeInstitution.objects.filter(id=attrs['type']):
            raise serializers.ValidationError(error_message.not_found('Type Institution'))
        return attrs'''
    
    def update(self, instance, validated_data):
        #county_id = validated_data['county'] if validated_data['county'] != None else 
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.county = County.objects.get(id=validated_data['county']) if validated_data['county'] != None else instance.county
        instance.street = validated_data.get('street', instance.street)
        #instance.code = validated_data.get('code', instance.code)
        instance.type = TypeInstitution.objects.get(id=validated_data['type']) if validated_data['type'] != None else instance.type
        #instance.update_date = dt.now()
        instance.update_date = timezone.now()
        
        instance.save()
        
        return instance

