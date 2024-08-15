from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import FindPastoralCoordinationSerializer, SavePastoralCoordinationSerializer, ListPastoralCoordinationSerializer, UpdatePastoralCoordinationSerializer, RenewalDatePastoralCoordinationSerializer
from .models import PastoralCoordination
from utils.message_error import ErrorMessage
import logging


logger = logging.getLogger(__name__)

# Create your views here.

class PastoralCoordinationRepository:
    def get_pastoral_coordination(self, pk: int):
        try:
            return PastoralCoordination.objects.get(id=pk)
        except PastoralCoordination.DoesNotExist:
            return None


class SavePastoralCoordinationView(generics.CreateAPIView):
    #queryset = m.PastoralCoordination.objects.all()
    error_message = ErrorMessage
    serializer_class = SavePastoralCoordinationSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Coordenação da Pastoral'
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


class ListPastoralCoordinationView(generics.ListAPIView):
    queryset = PastoralCoordination.objects.all()
    serializer_class = ListPastoralCoordinationSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Coordenação da Pastoral'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindPastoralCoordinationView(generics.RetrieveAPIView):
    queryset = PastoralCoordination.objects.all()
    serializer_class = FindPastoralCoordinationSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = PastoralCoordinationRepository()
    
    def get(self, request, id: int):
        OBJECTO = 'Coordenação da Pastoral'
        try:
            pastoral_coordination = self.repository.get_pastoral_coordination(id)
            
            if not pastoral_coordination:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(pastoral_coordination)
            logger.info(self.error_message.list_success_log(self, OBJECTO, 1))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePastoralCoordinationView(generics.UpdateAPIView):
    #queryset = m.PastoralCoordination.objects.all()
    error_message = ErrorMessage
    serializer_class = UpdatePastoralCoordinationSerializer
    permission_classes = [permissions.AllowAny]
    repository = PastoralCoordinationRepository()
    
    def update(self, request, id: int):
        OBJECTO = 'Coordenação da Pastoral'
        try:
            
            pastoral_coordination = self.repository.get_pastoral_coordination(id)
            
            if not pastoral_coordination:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message': self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(pastoral_coordination, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_409_CONFLICT)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class DeletePastoralCoordinationView(generics.DestroyAPIView):
    #queryset = PastoralCoordination.objects.all()
    serializer_class = ListPastoralCoordinationSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = PastoralCoordinationRepository()
    
    def delete(self, request, id: int, **kwargs):
        OBJECTO = 'Coordenação da Pastoral'
        
        try:
            pastoral_coordination = self.repository.get_pastoral_coordination(id)
            
            if not pastoral_coordination:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(pastoral_coordination)
            pastoral_coordination.delete()
            logger.warning(self.error_message.delete_sucess_log(self, OBJECTO, id))
            return Response({'data': serializer.data, 'message':self.error_message.delete_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.delete_error_log(self, OBJECTO, id, ex))
            return Response({'message': self.error_message.delete_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class RenewalDatePastoralCoordinationView(generics.UpdateAPIView):
    #queryset = m.PastoralCoordination.objects.all()
    error_message = ErrorMessage
    serializer_class = RenewalDatePastoralCoordinationSerializer
    permission_classes = [permissions.AllowAny]
    repository = PastoralCoordinationRepository()
    
    def update(self, request, id: int):
        OBJECTO = 'Coordenação da Pastoral'
        try:
            
            pastoral_coordination = self.repository.get_pastoral_coordination(id)
            
            if not pastoral_coordination:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message': self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(pastoral_coordination, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_409_CONFLICT)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


