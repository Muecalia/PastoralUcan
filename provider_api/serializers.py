from rest_framework import serializers
from .models import Provider
from institution_api.models import Institution
from institution_api.serializers import SaveInstitutionSerializer, UpdateInstitutionSerializer, ListInstitutionSerializer
from utils import code_error, message_error
from django.utils import timezone

class SaveProviderSerializer(serializers.ModelSerializer):
    institution = SaveInstitutionSerializer()
    
    class Meta:
        model = Provider
        fields = ['nif', 'institution']
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()        
        if Provider.objects.filter(nif=attrs['nif']).exists():
            raise serializers.ValidationError(error_message.exists('NIF'))
        
        return super().validate(attrs)

    def create(self, validated_data):
        institution_serializer = SaveInstitutionSerializer(data=validated_data['institution'])
        
        if institution_serializer.is_valid():
            institution_serializer.save()            

            data = {
                'nif': validated_data['nif'],
                'institution': Institution.objects.get(name=institution_serializer.data['name'])
            }
            
            provider = Provider.objects.create(**data)
            return provider        
        return None


class ListProviderSerializer(serializers.ModelSerializer):
    institution = serializers.SlugRelatedField(queryset=Institution.objects.all(), slug_field='name')
    
    class Meta:
        model = Provider
        fields = '__all__'


class UpdateProviderSerializer(serializers.ModelSerializer):
    institution = UpdateInstitutionSerializer()
    
    class Meta:
        model = Provider
        fields = ['nif', 'institution']
    
    
    def update(self, instance, validated_data):
        institution_serializer = UpdateInstitutionSerializer(instance.institution, data=validated_data.pop('institution'))
            
        if institution_serializer.is_valid():
            institution_serializer.save()
            
            instance.nif = validated_data.get('nif', instance.nif)
            instance.update_date = timezone.now()
            #instance.update_date = calendar.timegm(time.gmtime())
            
            instance.save()
        
            return instance
        return None
