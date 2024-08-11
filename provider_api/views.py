from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import SaveProviderSerializer, ListProviderSerializer, UpdateProviderSerializer
from .models import Provider
from utils.message_error import ErrorMessage
import logging


logger = logging.getLogger(__name__)

# Create your views here.

class ProviderRepository:
    def get_provider(self, pk: int):
        try:
            return Provider.objects.get(id=pk)
        except Provider.DoesNotExist:
            return None


class SaveProviderView(generics.CreateAPIView):
    #queryset = m.Provider.objects.all()
    error_message = ErrorMessage
    serializer_class = SaveProviderSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Provider'
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


class ListProviderView(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ListProviderSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Provider'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindProviderView(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ListProviderSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = ProviderRepository()
    
    def get(self, request, id: int, **kwargs):
        OBJECTO = 'Provider'
        
        try:
            provider = self.repository.get_provider(id)
            
            if not provider:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(provider)
            logger.warning(self.error_message.list_success_log(self, OBJECTO, 1))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateProviderView(generics.UpdateAPIView):
    error_message = ErrorMessage
    queryset = Provider.objects.all()
    serializer_class = UpdateProviderSerializer
    permission_classes = [permissions.AllowAny]
    repository = ProviderRepository()
    
    def update(self, request, id: int, **kwargs):
        OBJECTO = 'Provider'
        
        try:
            provider = self.repository.get_provider(id)
            
            if not provider:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)   
        
            serializer = self.serializer_class(provider, data=request.data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)
        

class DeleteProviderView(generics.DestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ListProviderSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = ProviderRepository()
    
    def delete(self, request, id: int, **kwargs):
        OBJECTO = 'Provider'
        
        try:
            provider = self.repository.get_provider(id)
            
            if not provider:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(provider)
            provider.delete()
            logger.warning(self.error_message.delete_sucess_log(self, OBJECTO, id))
            return Response({'data': serializer.data, 'message':self.error_message.delete_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.delete_error_log(self, OBJECTO, id, ex))
            return Response({'message': self.error_message.delete_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)
