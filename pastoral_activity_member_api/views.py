from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import FindPastoralActivityMemberSerializer, ListPastoralActivityMemberSerializer, SavePastoralActivityMemberSerializer, SavePastoralActivityVisitorSerializer, UpdatePastoralActivityMemberSerializer
from .models import PastoralActivityMember
from utils.message_error import ErrorMessage
import logging


logger = logging.getLogger(__name__)

# Create your views here.
class PastoralActivityMemberRepository:
    def get_pastoral_member(self, pk: int):
        try:
            return PastoralActivityMember.objects.get(id=pk)
        except PastoralActivityMember.DoesNotExist:
            return None


class SavePastoralActivityMemberView(generics.CreateAPIView):
    #queryset = m.PastoralActivityMember.objects.all()
    error_message = ErrorMessage
    serializer_class = SavePastoralActivityMemberSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Membro da Pastoral'
        try:
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.insert_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.insert_success(self, OBJECTO)}, status=status.HTTP_201_CREATED)
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            logger.error(self.error_message.insert_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.insert_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class SavePastoralActivityVisitorView(generics.CreateAPIView):
    #queryset = m.PastoralActivityMember.objects.all()
    error_message = ErrorMessage
    serializer_class = SavePastoralActivityVisitorSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Visitante da Pastoral'
        try:
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.insert_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.insert_success(self, OBJECTO)}, status=status.HTTP_201_CREATED)
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            logger.error(self.error_message.insert_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.insert_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class ListPastoralActivityMemberView(generics.ListAPIView):
    queryset = PastoralActivityMember.objects.all()
    serializer_class = ListPastoralActivityMemberSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Membro da Pastoral'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePastoralActivityMemberView(generics.UpdateAPIView):
    error_message = ErrorMessage
    queryset = PastoralActivityMember.objects.all()
    serializer_class = UpdatePastoralActivityMemberSerializer
    permission_classes = [permissions.AllowAny]
    repository = PastoralActivityMemberRepository()
    
    def update(self, request, id: int, **kwargs):
        OBJECTO = 'Membro da Pastoral'
        
        try:
            pastoral_activity_member = self.repository.get_pastoral_member(id)
            
            if not pastoral_activity_member:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)   
        
            serializer = self.serializer_class(pastoral_activity_member, data=request.data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindPastoralActivityMemberView(generics.ListAPIView):
    queryset = PastoralActivityMember.objects.all()
    serializer_class = FindPastoralActivityMemberSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = PastoralActivityMemberRepository()
    
    def get(self, request, id: int, **kwargs):
        OBJECTO = 'Membro da Pastoral'
        
        try:
            agreement = self.repository.get_pastoral_member(id)
            
            if not agreement:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(agreement)
            logger.warning(self.error_message.list_success_log(self, OBJECTO, 1))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)

