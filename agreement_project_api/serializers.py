from rest_framework import serializers
from .models import AgreementProject, StateProjectEnum
from agreement_api.models import Agreement
from utils import code_error, message_error
from django.utils import timezone, dateparse

class SaveAgreementProjectSerializer(serializers.ModelSerializer):
    start_date = serializers.CharField(write_only=True)
    end_date = serializers.CharField(write_only=True)
    agreement = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = AgreementProject
        fields = ('description_project', 'start_date', 'end_date','agreement')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        '''state = (item for item in list(StateProjectEnum) if item.value == attrs['state_project'])
        if len(list(state)) <= 0:
            raise serializers.ValidationError(error_message.not_found('state project'))'''
        
        if not Agreement.objects.filter(id=attrs['agreement']).exists():
            raise serializers.ValidationError(error_message.not_found('Agreement'))
        
        return super().validate(attrs)
        

    def create(self, validated_data):

        data = {
            'description_project': validated_data['description_project'],
            #'state_project': validated_data['state_project'],
            'state_project': 4,
            'start_date': dateparse.parse_datetime(validated_data['start_date']),
            'end_date': dateparse.parse_datetime(validated_data['end_date']),
            'agreement': Agreement.objects.get(id=validated_data['agreement'])
        }
        
        agreement_project = AgreementProject.objects.create(**data)
        return agreement_project


class ListAgreementProjectSerializer(serializers.ModelSerializer):
    #institution = serializers.SlugRelatedField(queryset=Institution.objects.all(), slug_field='name')
    
    class Meta:
        model = AgreementProject
        fields = '__all__'


class UpdateAgreementProjectSerializer(serializers.ModelSerializer):
    start_date = serializers.CharField(write_only=True)
    end_date = serializers.CharField(write_only=True)
    agreement = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = AgreementProject
        fields = ('description_project', 'state_project', 'start_date', 'end_date','agreement')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        '''
        if attrs['state_project'] not in list(StateProjectEnum.value):
            raise serializers.ValidationError(error_message.not_found('state project'))
        '''        
        state = (item for item in list(StateProjectEnum) if item.value == attrs['state_project'])
        if len(list(state)) <= 0:
            raise serializers.ValidationError(error_message.not_found('state project'))
        if Agreement.objects.filter(id=attrs['agreement']).exists():
            raise serializers.ValidationError(error_message.not_found('Agreement'))
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        instance.description_project = validated_data.get('description_project', instance.description_project)
        instance.state_project = validated_data.get('state_project', instance.state_project)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.agreement = instance.agreement if validated_data['agreement'] is None else Agreement.objects.get(id=validated_data['agreement'])
        instance.update_date = timezone.now()
        
        instance.save()

        return instance


class ChangeStateProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AgreementProject
        fields = ['state_project']
    
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        state = (item for item in list(StateProjectEnum) if item.value == attrs['state_project'])
        if len(list(state)) <= 0:
            raise serializers.ValidationError(error_message.not_found('state project'))
        
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        instance.state_project = validated_data.get('state_project', instance.state_project)
        instance.update_date = timezone.now()
        #instance.end_date = timezone.now()
        
        instance.save()
        
        return instance
    