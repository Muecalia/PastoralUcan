from rest_framework import serializers
from utils import code_error, message_error
from .models import PastoralMemberHasGroup, PastoralGroup, PastoralMember


class SavePastoralMemberHasGroupSerializer(serializers.ModelSerializer):
    pastoral_member = serializers.IntegerField()
    pastoral_group = serializers.IntegerField()
    
    class Meta:
        model = PastoralMemberHasGroup
        fields = ('pastoral_member', 'pastoral_group')


    def validate(self, attrs):
        error_message = message_error.ErrorMessage()
        if not PastoralMember.objects.filter(id=attrs['pastoral_member']).exists():
            raise serializers.ValidationError(error_message.not_found('Membro da Pastoral'))
        if not PastoralGroup.objects.filter(id=attrs['pastoral_group']).exists():
            raise serializers.ValidationError(error_message.not_found('Grupo da Pastoral'))
        
        return super().validate(attrs)

    
    def create(self, validated_data):
        
        data = {
            'pastoral_member': PastoralMember.objects.get(id=validated_data['pastoral_member']),
            'pastoral_group': PastoralGroup.objects.get(id=validated_data['pastoral_group'])
        }
        
        group = PastoralMemberHasGroup.objects.create(**data)
        return group
    

class ListPastoralMemberHasGroupSerializer(serializers.ModelSerializer):
    pastoral_member = serializers.SlugRelatedField(queryset=PastoralMember.objects.all(), slug_field='first_name')
    pastoral_group = serializers.SlugRelatedField(queryset=PastoralGroup.objects.all(), slug_field='name')
    
    class Meta:
        model = PastoralMemberHasGroup
        fields = '__all__'
        



