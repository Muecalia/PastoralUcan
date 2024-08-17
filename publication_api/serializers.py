from rest_framework import serializers
from .models import PastoralActivity, Publication
from utils import code_error, message_error
from django.utils import timezone



class SavePublicationSerializer(serializers.ModelSerializer):
    pastoral_activity = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Publication
        fields = ['title', 'path_photo', 'pastoral_activity', 'description']
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['title']) <= 0:
            raise serializers.ValidationError(error_message.error_size(attrs['title']))
        if Publication.objects.filter(title=attrs['title'], status=True).exists():
            raise serializers.ValidationError(error_message.exists(attrs['title']))
        if not PastoralActivity.objects.filter(id=attrs['pastoral_activity']).exists():
            raise serializers.ValidationError(error_message.not_found(attrs['pastoral_activity']))
        
        return super().validate(attrs)

    def create(self, validated_data):
        data = {
            'title': validated_data['title'],
            'path_photo': validated_data['path_photo'],
            'description': validated_data['description'],
            #'pastoral_activity': validated_data['pastoral_activity']
            'pastoral_activity': PastoralActivity.objects.get(id=validated_data['pastoral_activity'])
        }
        
        publication = Publication.objects.create(**data)
        return publication


class ListPublicationSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Publication
        fields = '__all__'


class UpdatePublicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publication
        fields = ['title', 'path_photo', 'description']    
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['title']) <= 0:
            raise serializers.ValidationError(error_message.error_size(attrs['title']))
        '''if Publication.objects.filter(title=attrs['title']).exists():
            raise serializers.ValidationError(error_message.exists(attrs['title']))
        if not PastoralActivity.objects.filter(id=attrs['pastoral_activity']).exists():
            raise serializers.ValidationError(error_message.not_found(attrs['pastoral_activity']))'''
        
        return super().validate(attrs)
    
    def update(self, instance, validated_data):            
        instance.title = validated_data.get('title', instance.title)
        instance.path_photo = validated_data.get('path_photo', instance.path_photo)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_date = timezone.now()        
        instance.save()
        
        return instance


