from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import SavePublicationSerializer, ListPublicationSerializer, UpdatePublicationSerializer
from .models import Publication
from utils.message_error import ErrorMessage
import logging


logger = logging.getLogger(__name__)

# Create your views here.

class PublicationRepository:
    def get_publication(self, pk: int):
        try:
            return Publication.objects.get(id=pk)
        except Publication.DoesNotExist:
            return None


class SavePublicationView(generics.CreateAPIView):
    #queryset = m.Publication.objects.all()
    error_message = ErrorMessage
    serializer_class = SavePublicationSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request): 
        OBJECTO = 'Publicação'
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


class ListPublicationView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = ListPublicationSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Publicação'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindPublicationView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = ListPublicationSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = PublicationRepository()
    
    def get(self, request, id: int, **kwargs):
        OBJECTO = 'Publicação'
        
        try:
            publication = self.repository.get_publication(id)
            
            if not publication:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(publication)
            logger.warning(self.error_message.list_success_log(self, OBJECTO, 1))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePublicationView(generics.UpdateAPIView):
    error_message = ErrorMessage
    #queryset = Publication.objects.all()
    serializer_class = UpdatePublicationSerializer
    permission_classes = [permissions.AllowAny]
    repository = PublicationRepository()
    
    def update(self, request, id: int, **kwargs):
        OBJECTO = 'Publicação'
        
        try:
            publication = self.repository.get_publication(id)
            
            if not publication:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)   
        
            serializer = self.serializer_class(publication, data=request.data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class DeletePublicationView(generics.DestroyAPIView):
    #queryset = Publication.objects.all()
    serializer_class = ListPublicationSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = PublicationRepository()
    
    def delete(self, request, id: int, **kwargs):
        OBJECTO = 'Publicação'
        
        try:
            publication = self.repository.get_publication(id)
            
            if not publication:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(publication)
            publication.delete()
            logger.warning(self.error_message.delete_sucess_log(self, OBJECTO, id))
            return Response({'data': serializer.data, 'message':self.error_message.delete_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.delete_error_log(self, OBJECTO, id, ex))
            return Response({'message': self.error_message.delete_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


