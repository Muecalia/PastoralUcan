from rest_framework import serializers
from .models import PastoralActivity, PastoralActivityMember, PastoralCoordination, PastoralMember, StatusEnum, PastoralVisitor
from utils import code_error, message_error
from django.utils import timezone, dateparse


class SavePastoralActivityMemberSerializer(serializers.ModelSerializer):
    pastoral_activity = serializers.IntegerField(write_only=True)    
    pastoral_member = serializers.IntegerField(write_only=True)
    #start_date = serializers.CharField()
    #end_date = serializers.CharField()
    
    class Meta:
        model = PastoralActivityMember
        fields = ('pastoral_activity', 'pastoral_member')
        read_only_fields = ('start_date','end_date')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if attrs['pastoral_activity'] <= 0:
            raise serializers.ValidationError(error_message.error_size('Actividade da Pastoral'))        
        if not PastoralActivity.objects.filter(id=attrs['pastoral_activity']).exists():
            raise serializers.ValidationError(error_message.not_found('Actividade da Pastoral'))
        if not PastoralMember.objects.filter(id=attrs['pastoral_member']).exists():
            raise serializers.ValidationError(error_message.not_found('Membro da Pastoral'))
        
        return super().validate(attrs)

    def create(self, validated_data):
        pastoral_activity = PastoralActivity.objects.get(id=validated_data['pastoral_activity'])
        pastoral_member = PastoralMember.objects.get(id=validated_data['pastoral_member'])

        try:
            pastoral_member_activity = PastoralActivityMember.objects.get(pastoral_activity=pastoral_activity, pastoral_member=pastoral_member)
            if ((pastoral_member_activity) & (pastoral_member_activity.status_activity == StatusEnum.CANCELADO.value) & (pastoral_activity.state)):
                pastoral_member_activity.delete()
        except PastoralActivityMember.DoesNotExist:
            print('Registo não encontrado')
        
        data = {
            'pastoral_activity': pastoral_activity,
            'start_date': pastoral_activity.start_date,
            'end_date': pastoral_activity.end_date,
            'pastoral_member': pastoral_member
        }
        
        pastoral_activity = PastoralActivityMember.objects.create(**data)
        return pastoral_activity
 
    

class SavePastoralActivityVisitorSerializer(serializers.ModelSerializer):
    pastoral_activity = serializers.IntegerField(write_only=True)
    pastoral_visitor = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = PastoralActivityMember
        fields = ('pastoral_activity', 'pastoral_visitor')
        read_only_fields = ('start_date','end_date')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if attrs['pastoral_activity'] <= 0:
            raise serializers.ValidationError(error_message.error_size('Actividade da Pastoral'))        
        if not PastoralActivity.objects.filter(id=attrs['pastoral_activity']).exists():
            raise serializers.ValidationError(error_message.not_found('Actividade da Pastoral'))
        if not PastoralVisitor.objects.filter(id=attrs['pastoral_visitor']).exists():
            raise serializers.ValidationError(error_message.not_found('Visitante'))
        
        return super().validate(attrs)

    def create(self, validated_data):
        pastoral_activity = PastoralActivity.objects.get(id=validated_data['pastoral_activity'])
        pastoral_visitor = PastoralVisitor.objects.get(id=validated_data['pastoral_visitor'])        
        
        try:
            pastoral_member_activity = PastoralActivityMember.objects.get(pastoral_activity=pastoral_activity, pastoral_visitor=pastoral_visitor)
            if ((pastoral_member_activity) & (pastoral_member_activity.status_activity == StatusEnum.CANCELADO.value) & (pastoral_activity.state)):
                pastoral_member_activity.delete()
        except PastoralActivityMember.DoesNotExist:
            print('Registo não encontrado')
        
        data = {
            'pastoral_activity': pastoral_activity,
            'start_date': pastoral_activity.start_date,
            'end_date': pastoral_activity.end_date,
            'pastoral_visitor': pastoral_visitor
        }
        
        pastoral_activity = PastoralActivityMember.objects.create(**data)
        return pastoral_activity


class ListPastoralActivityMemberSerializer(serializers.ModelSerializer):
    pastoral_activity = serializers.SlugRelatedField(queryset=PastoralActivityMember.objects.all(), slug_field='name')
    pastoral_coordination = serializers.SlugRelatedField(queryset=PastoralCoordination.objects.all(), slug_field='first_name')
    pastoral_member = serializers.SlugRelatedField(queryset=PastoralMember.objects.all(), slug_field='first_name')
    
    class Meta:
        model = PastoralActivityMember
        fields = '__all__'


class FindPastoralActivityMemberSerializer(serializers.ModelSerializer):
    pastoral_activity = serializers.SlugRelatedField(queryset=PastoralActivityMember.objects.all(), slug_field='name')
    pastoral_coordination = serializers.SlugRelatedField(queryset=PastoralCoordination.objects.all(), slug_field='first_name')
    pastoral_member = serializers.SlugRelatedField(queryset=PastoralMember.objects.all(), slug_field='first_name')
    
    class Meta:
        model = PastoralActivityMember
        fields = '__all__'


class UpdatePastoralActivityMemberSerializer(serializers.ModelSerializer):
    pastoral_coordination = serializers.IntegerField(write_only=True)
    #pastoral_coordination = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = PastoralActivityMember
        fields = ('pastoral_coordination', 'status_activity', 'payment')
    
    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        status = (item for item in list(StatusEnum) if item.value == attrs['status_activity'])
        if len(list(status)) <= 0:
            raise serializers.ValidationError(error_message.not_found('Estado do Pagamento'))
        if attrs['pastoral_coordination'] <= 0:
            raise serializers.ValidationError(error_message.error_size('Coordenação da Pastoral'))
        if attrs['payment'] < 0:
            raise serializers.ValidationError(error_message.error_payment('Pagamento'))
        if not PastoralCoordination.objects.filter(id=attrs['pastoral_coordination']).exists():
            raise serializers.ValidationError(error_message.not_found('Coordenação da Pastoral'))
        
        return super().validate(attrs)
    

    def update(self, instance, validated_data):        
        instance.status = True
        instance.payment = (instance.payment + validated_data['payment']) if StatusEnum.CANCELADO.value != validated_data['status_activity'] else instance.payment * (-1)
        instance.status_activity = validated_data['status_activity']
        instance.pastoral_coordination = PastoralCoordination.objects.get(id=validated_data['pastoral_coordination'])        
        instance.updated_date = timezone.now()
        
        instance.save()
        return instance
        
   