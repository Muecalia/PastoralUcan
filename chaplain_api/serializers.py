from rest_framework import serializers
from .models import Chaplain, PastoralMember, Congregation
from pastoral_member_api.serializers import ListPastoralMemberSerializer, SavePastoralMemberSerializer, UpdatePastoralMemberSerializer
#from institution_api.serializers import SaveInstitutionSerializer, UpdateInstitutionSerializer, ListInstitutionSerializer
from utils import code_error, message_error
from django.utils import timezone, dateparse


class SaveChaplainSerializer(serializers.ModelSerializer):
    congregation = serializers.IntegerField(write_only=True)
    pastoral_member = SavePastoralMemberSerializer()
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    
    class Meta:
        model = Chaplain
        #fields = ['name', 'description', 'institution']
        fields = ['pastoral_member', 'congregation', 'start_date', 'end_date']
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if (len(attrs['start_date']) > 0) &  (not dateparse.parse_datetime(attrs['start_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de início do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        if not Congregation.objects.filter(id=attrs['congregation']).exists():
            raise serializers.ValidationError(error_message.not_found('Congregação'))
        if dateparse.parse_datetime(attrs['start_date']) > dateparse.parse_datetime(attrs['end_date']):
            raise serializers.ValidationError(error_message.date_error(attrs['start_date'], attrs['end_date']))
        
        return super().validate(attrs)

    def create(self, validated_data):
        pastoral_member_serializer = SavePastoralMemberSerializer(data=validated_data['pastoral_member'])
        
        if pastoral_member_serializer.is_valid():
            pastoral_member_serializer.save()
            print(f'pastoral_member: {pastoral_member_serializer.data}')
            data = {
                #'name': validated_data['name'],
                'profile_id': 1,
                'congregation': Congregation.objects.get(id=validated_data['congregation']),
                'pastoral_member': PastoralMember.objects.get(first_name=pastoral_member_serializer.data['first_name'], last_name=pastoral_member_serializer.data['last_name']),
                'start_date': dateparse.parse_datetime(validated_data['start_date']),
                'end_date': dateparse.parse_datetime(validated_data['end_date']),
            }
            
            chaplain = Chaplain.objects.create(**data)
            return chaplain
        return pastoral_member_serializer.errors


class ListChaplainSerializer(serializers.ModelSerializer):
    pastoral_member = serializers.SlugRelatedField(queryset=PastoralMember.objects.all(), slug_field='first_name')
    congregation = serializers.SlugRelatedField(queryset=Congregation.objects.all(), slug_field='name')
    
    class Meta:
        model = Chaplain
        fields = '__all__'


class FindChaplainSerializer(serializers.ModelSerializer):
    #pastoral_member = serializers.SlugRelatedField(queryset=PastoralMember.objects.all(), slug_field='first_name')
    congregation = serializers.SlugRelatedField(queryset=Congregation.objects.all(), slug_field='name')
    
    class Meta:
        model = Chaplain
        fields = '__all__'


class UpdateChaplainSerializer(serializers.ModelSerializer):
    congregation = serializers.IntegerField(write_only=True)
    pastoral_member = UpdatePastoralMemberSerializer()
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    
    class Meta:
        model = Chaplain
        fields = ['pastoral_member', 'congregation', 'start_date', 'end_date']
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if (len(attrs['start_date']) > 0) &  (not dateparse.parse_datetime(attrs['start_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de início do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        if not Congregation.objects.filter(id=attrs['congregation']).exists():
            raise serializers.ValidationError(error_message.not_found('Congregação'))
        if dateparse.parse_datetime(attrs['start_date']) > dateparse.parse_datetime(attrs['end_date']):
            raise serializers.ValidationError(error_message.date_error(attrs['start_date'], attrs['end_date']))
        
        return super().validate(attrs)

    def update(self, instance, validated_data):
        pastoral_member_serializer = UpdatePastoralMemberSerializer(instance=instance.pastoral_member, data=validated_data.get('pastoral_member'))
        
        if pastoral_member_serializer.is_valid():
            pastoral_member_serializer.save()
            print(f'pastoral_member: {pastoral_member_serializer.data}')
            
            instance.congregation = Congregation.objects.get(id=validated_data['congregation'])
            instance.start_date = dateparse.parse_datetime(validated_data['start_date'])
            instance.end_date = dateparse.parse_datetime(validated_data['end_date'])            
            instance.updated_date = timezone.now()
            
            instance.save()
            return instance
        return pastoral_member_serializer.errors
        
        
class RenewalDateChaplainSerializer(serializers.ModelSerializer):
    end_date = serializers.CharField()
    
    class Meta:
        model = Chaplain
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

