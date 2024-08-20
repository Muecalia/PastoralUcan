from rest_framework import serializers
from .models import PastoralVisitor
from utils import code_error, message_error
from django.utils import timezone, dateparse


class ListPastoralVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastoralVisitor
        fields = '__all__'
        #now.strftime("%d/%m/%Y, %H:%M:%S")


class SavePastoralVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastoralVisitor
        fields = ('name', 'email','phone')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['name']) <= 0:
            raise serializers.ValidationError(error_message.error_size(attrs['name']))        
        if PastoralVisitor.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(error_message.exists(attrs['email']))
        if PastoralVisitor.objects.filter(phone=attrs['phone']).exists():
            raise serializers.ValidationError(error_message.exists(attrs['phone']))
        return attrs
        
    def create(self, validated_data):
        data = {
            'name': validated_data['name'],
            'email': validated_data['email'],
            'phone': validated_data['phone']
        }
        
        pastoral_member = PastoralVisitor.objects.create(**data)
        
        return pastoral_member


class UpdatePastoralVisitorSerializer(serializers.ModelSerializer):    
    class Meta:
        model = PastoralVisitor
        fields = ('name', 'email','phone')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['name']) <= 0:
            raise serializers.ValidationError(error_message.error_size(attrs['name']))        
        if PastoralVisitor.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(error_message.exists(attrs['email']))
        if PastoralVisitor.objects.filter(phone=attrs['phone']).exists():
            raise serializers.ValidationError(error_message.exists(attrs['phone']))
        return attrs
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)        
        instance.updated_date = timezone.now()
        instance.save()
        
        return instance

