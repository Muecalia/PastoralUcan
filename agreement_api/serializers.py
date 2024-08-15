from rest_framework import serializers
from .models import Agreement
from institution_api.models import Institution
from institution_api.serializers import SaveInstitutionSerializer, UpdateInstitutionSerializer, ListInstitutionSerializer
from utils import code_error, message_error
from django.utils import timezone

class SaveAgreementSerializer(serializers.ModelSerializer):
    institution = SaveInstitutionSerializer()
    #county = serializers.IntegerField(write_only=True)
    #type = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Agreement
        #fields = ['name', 'description', 'institution']
        fields = ['description', 'institution']
    
    '''def validate(self, attrs):
        error_message = message_error.ErrorMessage()        
        if Agreement.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError(error_message.exists('name'))
        
        return super().validate(attrs)'''

    def create(self, validated_data):
        institution_serializer = SaveInstitutionSerializer(data=validated_data['institution'])
        
        if institution_serializer.is_valid():
            institution_serializer.save()            

            data = {
                #'name': validated_data['name'],
                'description': validated_data['description'],
                'institution': Institution.objects.get(name=institution_serializer.data['name'])
            }
            
            agreement = Agreement.objects.create(**data)
            return agreement        
        return None


class ListAgreementSerializer(serializers.ModelSerializer):
    institution = serializers.SlugRelatedField(queryset=Institution.objects.all(), slug_field='name')
    
    class Meta:
        model = Agreement
        fields = '__all__'


class UpdateAgreementSerializer(serializers.ModelSerializer):
    institution = UpdateInstitutionSerializer()
    
    class Meta:
        model = Agreement
        fields = ['description', 'institution']
    
    
    def update(self, instance, validated_data):
        institution_serializer = UpdateInstitutionSerializer(instance.institution, data=validated_data.pop('institution'))
            
        if institution_serializer.is_valid():
            institution_serializer.save()
            
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.update_date = timezone.now()
            #instance.update_date = calendar.timegm(time.gmtime())
            
            instance.save()
        
            return instance
        return institution_serializer.errors


