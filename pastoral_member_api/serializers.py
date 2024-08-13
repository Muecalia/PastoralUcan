from rest_framework import serializers
from .models import PastoralMember
from address_api.models import Country, County
from religion_api.models import Religion, Sacrament
from general_api.models import AcademicLevel, School, University
from utils import code_error, message_error
from django.utils import timezone, dateparse


class ListPastoralMemberSerializer(serializers.ModelSerializer):
    #data = serializers.SlugRelatedField()
    class Meta:
        model = PastoralMember
        fields = ('first_name', 'last_name', 'email','phone', 'created_date')
        #now.strftime("%d/%m/%Y, %H:%M:%S")


class FindPastoralMemberSerializer(serializers.ModelSerializer):
    #data = serializers.SlugRelatedField()
    nacionality = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='name')
    religion = serializers.SlugRelatedField(queryset=Religion.objects.all(), slug_field='name')
    sacrament = serializers.SlugRelatedField(queryset=Sacrament.objects.all(), slug_field='name')
    academic_level = serializers.SlugRelatedField(queryset=AcademicLevel.objects.all(), slug_field='name')
    school = serializers.SlugRelatedField(queryset=School.objects.all(), slug_field='name')
    university = serializers.SlugRelatedField(queryset=University.objects.all(), slug_field='name')
    county = serializers.SlugRelatedField(queryset=County.objects.all(), slug_field='name')
    #birth_date = serializers.StringRelatedField(write_only=True)
    #gender
    #civil_state
    
    #institution = 
    
    
    class Meta:
        model = PastoralMember
        fields = '__all__'
        #now.strftime("%d/%m/%Y, %H:%M:%S") myDate.strftime('%m/%d/%Y')


class SavePastoralMemberSerializer(serializers.ModelSerializer):    
    class Meta:
        model = PastoralMember
        fields = ('first_name', 'last_name', 'email','phone')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if len(attrs['first_name']) <= 0:
            raise serializers.ValidationError(error_message.error_size('Primeiro nome'))
        if len(attrs['last_name']) <= 0:
            raise serializers.ValidationError(error_message.error_size('Último nome'))
        if PastoralMember.objects.filter(first_name=attrs['first_name'], last_name=attrs['last_name']).exists():
            raise serializers.ValidationError(error_message.exists(attrs['first_name'] + ' ' + attrs['last_name']))
        if PastoralMember.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(error_message.exists('email'))
        if PastoralMember.objects.filter(phone=attrs['phone']).exists():
            raise serializers.ValidationError(error_message.exists('phone'))
        return attrs
        
    def create(self, validated_data):        
        data = {
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'email': validated_data['email'],
            'phone': validated_data['phone']
        }
        
        pastoral_member = PastoralMember.objects.create(**data)
        
        return pastoral_member


class UpdatePastoralMemberSerializer(serializers.ModelSerializer):
    nacionality = serializers.IntegerField(write_only=True)
    religion = serializers.IntegerField(write_only=True)
    sacrament = serializers.IntegerField(write_only=True)
    academic_level = serializers.IntegerField(write_only=True)
    school = serializers.IntegerField(write_only=True)
    university = serializers.IntegerField(write_only=True)
    county = serializers.IntegerField(write_only=True)
    birth_date = serializers.CharField(write_only=True)
    
    class Meta:
        model = PastoralMember
        fields = '__all__'
        read_only_fields = ('created_date','updated_date', 'state')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()     
        if len(attrs['first_name']) <= 0:
            raise serializers.ValidationError(error_message.error_size('Primeiro nome'))
        if len(attrs['last_name']) <= 0:
            raise serializers.ValidationError(error_message.error_size('Último nome'))
        if len(attrs['phone']) <= 0:
            raise serializers.ValidationError(error_message.error_size('Telefone'))
        if len(attrs['email']) <= 0:
            raise serializers.ValidationError(error_message.error_size('email'))
        if (len(attrs['birth_date']) > 0) &  (not dateparse.parse_datetime(attrs['birth_date'])):
            raise serializers.ValidationError(error_message.date_formate('Data de nascimento'))
        
        return attrs
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.birth_date = dateparse.parse_datetime(validated_data['birth_date']) if validated_data['birth_date'] != None else instance.birth_date
        instance.nacionality = Country.objects.get(id=validated_data['nacionality']) if validated_data['nacionality'] > 0 else instance.nacionality
        instance.religion = Religion.objects.get(id=validated_data['religion']) if validated_data['religion'] > 0 else instance.religion
        instance.sacrament = Sacrament.objects.get(id=validated_data['sacrament']) if validated_data['sacrament'] > 0 else instance.sacrament
        instance.academic_level = AcademicLevel.objects.get(id=validated_data['academic_level']) if validated_data['academic_level'] > 0 else instance.academic_level
        instance.school = School.objects.get(id=validated_data['school']) if validated_data['school'] > 0 else instance.school
        instance.university = University.objects.get(id=validated_data['university']) if validated_data['university'] > 0 else instance.university
        instance.county = County.objects.get(id=validated_data['county']) if validated_data['county'] > 0 else instance.county
        instance.gender = validated_data.get('gender', instance.gender)
        instance.civil_state = validated_data.get('civil_state', instance.civil_state)
        instance.street = validated_data.get('street', instance.street)
        instance.house_number = validated_data.get('house_number', instance.house_number)
        instance.updated_date = timezone.now()
        instance.save()
        
        return instance

