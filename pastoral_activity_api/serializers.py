from rest_framework import serializers
from .models import PastoralActivity, TypeActivity
from utils import code_error, message_error
from django.utils import timezone, dateparse


class SavePastoralActivitySerializer(serializers.ModelSerializer):
    type_activity = serializers.IntegerField(write_only=True)
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    
    class Meta:
        model = PastoralActivity
        fields = '__all__'
        read_only_fields = ('created_date','updated_date', 'state')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['name']) <= 0:
            raise serializers.ValidationError(error_message.error_size(attrs['name']))
        if (len(attrs['start_date']) > 0) &  (not dateparse.parse_datetime(attrs['start_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de início do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        if not TypeActivity.objects.filter(id=attrs['type_activity']).exists():
            raise serializers.ValidationError(error_message.not_found('Congregação'))
        if dateparse.parse_datetime(attrs['start_date']) > dateparse.parse_datetime(attrs['end_date']):
            raise serializers.ValidationError(error_message.date_error(attrs['start_date'], attrs['end_date']))
        
        return super().validate(attrs)

    def create(self, validated_data):
        data = {
            'name': validated_data['name'],
            'description': validated_data['description'],
            'type_activity': TypeActivity.objects.get(id=validated_data['type_activity']),
            'start_date': dateparse.parse_datetime(validated_data['start_date']),
            'end_date': dateparse.parse_datetime(validated_data['end_date']),
        }
        
        pastoral_activity = PastoralActivity.objects.create(**data)
        return pastoral_activity


class ListPastoralActivitySerializer(serializers.ModelSerializer):
    type_activity = serializers.SlugRelatedField(queryset=TypeActivity.objects.all(), slug_field='name')
    
    class Meta:
        model = PastoralActivity
        fields = '__all__'


class FindPastoralActivitySerializer(serializers.ModelSerializer):
    type_activity = serializers.SlugRelatedField(queryset=TypeActivity.objects.all(), slug_field='name')
    
    class Meta:
        model = PastoralActivity
        fields = '__all__'


class UpdatePastoralActivitySerializer(serializers.ModelSerializer):
    type_activity = serializers.IntegerField(write_only=True)
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    
    class Meta:
        model = PastoralActivity
        fields = '__all__'
        read_only_fields = ('created_date','updated_date', 'state')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['name']) < 0:
            raise serializers.ValidationError(error_message.error_size(attrs['name']))
        if (len(attrs['start_date']) > 0) &  (not dateparse.parse_datetime(attrs['start_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de início do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        if not TypeActivity.objects.filter(id=attrs['type_activity']).exists():
            raise serializers.ValidationError(error_message.not_found('Congregação'))
        if dateparse.parse_datetime(attrs['start_date']) > dateparse.parse_datetime(attrs['end_date']):
            raise serializers.ValidationError(error_message.date_error(attrs['start_date'], attrs['end_date']))
        
        return super().validate(attrs)


    def update(self, instance, validated_data):            
        instance.name = validated_data.get('congregation', instance.name)
        instance.description = validated_data.get('congregation', instance.description)
        instance.type_activity = TypeActivity.objects.get(id=validated_data['type_activity'])
        instance.start_date = dateparse.parse_datetime(validated_data['start_date'])
        instance.end_date = dateparse.parse_datetime(validated_data['end_date'])            
        instance.updated_date = timezone.now()
        
        instance.save()
        return instance
        
   