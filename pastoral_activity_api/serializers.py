from rest_framework import serializers
from .models import PastoralActivity, TypeActivity, StatusEnum
from utils import code_error, message_error
from django.utils import timezone, dateparse
from publication_api.serializers import SavePublicationSerializer, UpdatePublicationSerializer, ListPublicationSerializer, Publication


class PublicationRepository:
    def find_publication_by_activity(self, pastotal_activity: PastoralActivity):
        try:
            return Publication.objects.get(pastoral_activity=pastotal_activity)
        except Publication.DoesNotExist:
            return None
        
    def update_publication_status(self, publication: Publication, status: bool):
        if publication:
            publication.status = status
            publication.save()  

class SavePastoralActivitySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()    
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    path_photo = serializers.CharField(write_only=True)
    type_activity = serializers.IntegerField(write_only=True)
        
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if PastoralActivity.objects.filter(name=attrs['name'], state=True).exists():
            raise serializers.ValidationError(error_message.exists(attrs['name']))
        if len(attrs['name']) <= 0:
            raise serializers.ValidationError(error_message.error_size(attrs['name']))
        if (len(attrs['start_date']) > 0) &  (not dateparse.parse_datetime(attrs['start_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de início do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        if not TypeActivity.objects.filter(id=attrs['type_activity']).exists():
            raise serializers.ValidationError(error_message.not_found('Tipo de actividade'))
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
        
        publication = {
            'title': pastoral_activity.name,
            'path_photo': validated_data['path_photo'],
            'pastoral_activity': pastoral_activity.pk,
            'description': pastoral_activity.description
        }
        
        publication_serializer = SavePublicationSerializer(data=publication)
        
        if publication_serializer.is_valid():
            publication_serializer.save()
            return pastoral_activity

        pastoral_activity.delete()
        print(publication_serializer.errors)
        return None
     

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


class UpdatePastoralActivitySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()    
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    path_photo = serializers.CharField(write_only=True)
    type_activity = serializers.IntegerField(write_only=True)
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['name']) < 0:
            raise serializers.ValidationError(error_message.error_size(attrs['name']))
        if (len(attrs['start_date']) > 0) &  (not dateparse.parse_datetime(attrs['start_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de início do mandato'))
        if (len(attrs['end_date']) > 0) &  (not dateparse.parse_datetime(attrs['end_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de fim do mandato'))
        if not TypeActivity.objects.filter(id=attrs['type_activity']).exists():
            raise serializers.ValidationError(error_message.not_found('Tipo de actividade'))
        if dateparse.parse_datetime(attrs['start_date']) > dateparse.parse_datetime(attrs['end_date']):
            raise serializers.ValidationError(error_message.date_error(attrs['start_date'], attrs['end_date']))
        
        return super().validate(attrs)


    def update(self, instance, validated_data):
        repository = PublicationRepository()
        
        publication = repository.find_publication_by_activity(instance)
        
        if not publication:
            print('Erro! Publicação não encontrada')
            return None
        
        print(f'name: {instance.name} - title: {publication.title}')
            
        publication_data = {
            'title': validated_data['name'],
            'path_photo': validated_data['path_photo'],
            'description': validated_data['description']
        }

        publication_serializer = UpdatePublicationSerializer(publication, data=publication_data, partial=True)
        
        if publication_serializer.is_valid():
            publication_serializer.save()
            
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.type_activity = TypeActivity.objects.get(id=validated_data['type_activity'])
            instance.start_date = dateparse.parse_datetime(validated_data['start_date'])
            instance.end_date = dateparse.parse_datetime(validated_data['end_date'])  
            instance.updated_date = timezone.now()
            
            instance.save()
            return instance       
        
        return publication_serializer.errors
   

class UpdatePastoralActivityStatusSerializer(serializers.ModelSerializer):    
    class Meta:
        model = PastoralActivity
        fields = ['status']
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if ((len(attrs['status']) <= 0) or (len(attrs['status']) > 2)):
            raise serializers.ValidationError(error_message.error_size('Estado'))
        if attrs['status'] == StatusEnum.CREATED.value:
            raise serializers.ValidationError(error_message.error_status('Estado da actividade'))
        
        status = (item for item in list(StatusEnum) if item.value == attrs['status'])        
        if len(list(status)) <= 0:
            raise serializers.ValidationError(error_message.not_found('Estado'))
        
        return super().validate(attrs)

    def update(self, instance, validated_data):
        repository = PublicationRepository()
        instance.status = validated_data.get('status', instance.status)
        
        publication = repository.find_publication_by_activity(instance)
        
        if validated_data['status'] == StatusEnum.PUBLISHED.value:
            instance.is_published = True
            instance.publication_date = timezone.now()
            repository.update_publication_status(publication, True)
            
        else:
            instance.suspended_date = timezone.now()
            repository.update_publication_status(publication, False)
                
        
        instance.save()
        return instance
 