from rest_framework import serializers
from .models import PastoralCoordination, PastoralMember
from pastoral_member_api.serializers import ListPastoralMemberSerializer
from utils import code_error, message_error
from django.utils import timezone, dateparse
from datetime import datetime


class SavePastoralCoordinationSerializer(serializers.ModelSerializer):
    pastoral_member = serializers.IntegerField(write_only=True)
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    profile_id = serializers.IntegerField()
    
    class Meta:
        model = PastoralCoordination
        #fields = ['name', 'description', 'institution']
        fields = ['pastoral_member', 'profile_id', 'start_date', 'end_date']
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if attrs['profile_id'] <= 0:
            raise serializers.ValidationError(error_message.not_found('Perfil'))
        if not PastoralMember.objects.filter(id=attrs['pastoral_member']).exists():
            raise serializers.ValidationError(error_message.not_found('Membro da Pastoral'))
        if (len(attrs['start_date']) > 0) &  (not dateparse.parse_datetime(attrs['start_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de início do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        if dateparse.parse_datetime(attrs['start_date']) > dateparse.parse_datetime(attrs['end_date']):
            raise serializers.ValidationError(error_message.date_error(attrs['start_date'], attrs['end_date']))
        
        
        return super().validate(attrs)

    def create(self, validated_data):
        data = {
            'profile_id': validated_data['profile_id'],
            'pastoral_member': PastoralMember.objects.get(id=validated_data['pastoral_member']),
            #'start_date': datetime.fromisoformat(validated_data['start_date']),
            #'end_date': datetime.fromisoformat(validated_data['end_date'])
            'start_date': dateparse.parse_datetime(validated_data['start_date']),
            'end_date': dateparse.parse_datetime(validated_data['end_date'])
        }
        #datetime.strptime('04/27/95 07:14:22', '%m/%d/%y %H:%M:%S')
        
        pastoral_coordination = PastoralCoordination.objects.create(**data)
        return pastoral_coordination


class ListPastoralCoordinationSerializer(serializers.ModelSerializer):
    pastoral_member = serializers.SlugRelatedField(queryset=PastoralMember.objects.all(), slug_field='first_name')
    
    class Meta:
        model = PastoralCoordination
        fields = '__all__'


class FindPastoralCoordinationSerializer(serializers.ModelSerializer):
    #pastoral_member = serializers.SlugRelatedField(queryset=PastoralMember.objects.all(), slug_field='first_name')
    
    class Meta:
        model = PastoralCoordination
        fields = '__all__'


class UpdatePastoralCoordinationSerializer(serializers.ModelSerializer):
    pastoral_member = serializers.IntegerField(write_only=True)
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    profile_id = serializers.IntegerField()
    
    class Meta:
        model = PastoralCoordination
        #fields = ['name', 'description', 'institution']
        fields = ['pastoral_member', 'profile_id', 'start_date', 'end_date']
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if attrs['profile_id'] < 0:
            raise serializers.ValidationError(error_message.not_found('Perfil'))
        if (len(attrs['start_date']) > 0) &  (not dateparse.parse_datetime(attrs['start_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de início do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        if dateparse.parse_datetime(attrs['start_date']) > dateparse.parse_datetime(attrs['end_date']):
            raise serializers.ValidationError(error_message.date_error(attrs['start_date'], attrs['end_date']))
        if not PastoralMember.objects.filter(id=attrs['pastoral_member']).exists():
            raise serializers.ValidationError(error_message.not_found('Membro da Pastoral'))
        
        return super().validate(attrs)

    def update(self, instance, validated_data):        
        instance.pastoral_member = PastoralMember.objects.get(id=validated_data['pastoral_member'])
        instance.start_date = dateparse.parse_datetime(validated_data['start_date'])
        instance.end_date = dateparse.parse_datetime(validated_data['end_date'])  
        instance.profile_id = validated_data.get('profile_id', instance.profile_id)
        instance.updated_date = timezone.now()
        
        instance.save()
        return instance


class RenewalDatePastoralCoordinationSerializer(serializers.ModelSerializer):
    end_date = serializers.CharField()
    
    class Meta:
        model = PastoralCoordination
        fields = ['end_date']
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['end_date']) < 0:
            raise serializers.ValidationError(error_message.error_size('Data de fim do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        
        return super().validate(attrs)

    def update(self, instance, validated_data):        
        instance.end_date = dateparse.parse_datetime(validated_data['end_date'])        
        instance.renewal_date = timezone.now()
        
        instance.save()
        return instance
        


