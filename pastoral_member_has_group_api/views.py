from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import ListPastoralMemberHasGroupSerializer, SavePastoralMemberHasGroupSerializer
from .models import PastoralMemberHasGroup, PastoralGroup, PastoralMember
from utils.message_error import ErrorMessage
import logging

logger = logging.getLogger(__name__)


# Create your views here.

class PastoralMemberHasGroupRepository:
    def get_pastoral_member_group(self, pk: int):
        try:
            return PastoralMemberHasGroup.objects.get(id=pk)
        except PastoralMemberHasGroup.DoesNotExist:
            return None


class SavePastoralMemberHasGroupView(generics.CreateAPIView):
    #queryset = m.PastoralMemberHasGroup.objects.all()
    error_message = ErrorMessage
    serializer_class = SavePastoralMemberHasGroupSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Grupos do Membro da Pastoral'
        try:
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.insert_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.insert_success(self, OBJECTO)}, status=status.HTTP_201_CREATED)
            return Response({'message':serializer.errors}, status=status.HTTP_409_CONFLICT)
        except Exception as ex:
            logger.error(self.error_message.insert_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.insert_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class ListPastoralMemberHasGroupView(generics.ListAPIView):
    queryset = PastoralMemberHasGroup.objects.all()
    serializer_class = ListPastoralMemberHasGroupSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Grupos do Membro da Pastoral'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class DeletePastoralMemberHasGroupView(generics.DestroyAPIView):
    #queryset = PastoralMemberHasGroup.objects.all()
    serializer_class = ListPastoralMemberHasGroupSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = PastoralMemberHasGroupRepository()
    
    def delete(self, request, id: int, **kwargs):
        OBJECTO = 'Grupos do Membro da Pastoral'
        
        try:
            pastoral_member_group = self.repository.get_pastoral_member_group(id)
            
            if not pastoral_member_group:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(pastoral_member_group)
            pastoral_member_group.delete()
            logger.warning(self.error_message.delete_sucess_log(self, OBJECTO, id))
            return Response({'data': serializer.data, 'message':self.error_message.delete_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.delete_error_log(self, OBJECTO, id, ex))
            return Response({'message': self.error_message.delete_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindPastoralMemberHasGroupByMemberView(generics.ListAPIView):
    queryset = PastoralMemberHasGroup.objects.all()
    serializer_class = ListPastoralMemberHasGroupSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, member_id: int, **kwargs):
        OBJECTO = 'Grupos do Membro da Pastoral'
        OBJECTO_MP = 'Membro da Pastoral'
        
        try:
            try:
                pastoral_member = PastoralMember.objects.get(id=member_id)
            except PastoralMember.DoesNotExist:
                logger.info(self.error_message.not_found_log(self, OBJECTO_MP, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO_MP)}, status=status.HTTP_404_NOT_FOUND)
            
            pastoral_member_group = self.queryset.filter(pastoral_member=pastoral_member)
            
            '''if not pastoral_member_group:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)'''
                
            serializer = self.serializer_class(pastoral_member_group, many=True)
            logger.warning(self.error_message.list_success_log(self, OBJECTO, len(pastoral_member_group)))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindPastoralMemberHasGroupByGroupView(generics.ListAPIView):
    queryset = PastoralMemberHasGroup.objects.all()
    serializer_class = ListPastoralMemberHasGroupSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, group_id: int):
        OBJECTO = 'Grupos do Membro da Pastoral'
        OBJECTO_GP = 'Grupo da Pastoral'
        
        try:            
            try:
                pastoral_group = PastoralGroup.objects.all().get(id=group_id)
            except PastoralGroup.DoesNotExist:
                logger.info(self.error_message.not_found_log(self, OBJECTO_GP, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO_GP)}, status=status.HTTP_404_NOT_FOUND)
                        
            pastoral_member_group = self.queryset.filter(pastoral_group=pastoral_group).all()
            
            '''if len(pastoral_member_group) < 0:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)'''
            
            serializer = self.serializer_class(pastoral_member_group, many=True)
            logger.warning(self.error_message.list_success_log(self, OBJECTO, len(pastoral_member_group)))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)
