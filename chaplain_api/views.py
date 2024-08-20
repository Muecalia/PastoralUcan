from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import FindChaplainSerializer, SaveChaplainSerializer, ListChaplainSerializer, UpdateChaplainSerializer, RenewalDateChaplainSerializer
from .models import Chaplain
from utils.message_error import ErrorMessage
import logging


logger = logging.getLogger(__name__)

# Create your views here.

class ChaplainRepository:
    def get_chaplain(self, pk: int):
        try:
            return Chaplain.objects.get(id=pk)
        except Chaplain.DoesNotExist:
            return None


class SaveChaplainView(generics.CreateAPIView):
    #queryset = m.Chaplain.objects.all()
    error_message = ErrorMessage
    serializer_class = SaveChaplainSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Capelão'
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


class ListChaplainView(generics.ListAPIView):
    queryset = Chaplain.objects.all()
    serializer_class = ListChaplainSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Capelão'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindChaplainView(generics.RetrieveAPIView):
    queryset = Chaplain.objects.all()
    serializer_class = FindChaplainSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = ChaplainRepository()
    
    def get(self, request, id: int):
        OBJECTO = 'Capelão'
        try:
            chaplain = self.repository.get_chaplain(id)
            
            if not chaplain:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(chaplain)
            logger.info(self.error_message.list_success_log(self, OBJECTO, 1))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateChaplainView(generics.UpdateAPIView):
    #queryset = m.Chaplain.objects.all()
    error_message = ErrorMessage
    serializer_class = UpdateChaplainSerializer
    permission_classes = [permissions.AllowAny]
    repository = ChaplainRepository()
    
    def update(self, request, id: int):
        OBJECTO = 'Capelão'
        try:
            
            chaplain = self.repository.get_chaplain(id)
            
            if not chaplain:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message': self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(chaplain, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_409_CONFLICT)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteChaplainView(generics.DestroyAPIView):
    #queryset = Chaplain.objects.all()
    serializer_class = ListChaplainSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = ChaplainRepository()
    
    def delete(self, request, id: int, **kwargs):
        OBJECTO = 'Capelão'
        
        try:
            chaplain = self.repository.get_chaplain(id)
            
            if not chaplain:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(chaplain)
            chaplain.delete()
            logger.warning(self.error_message.delete_sucess_log(self, OBJECTO, id))
            return Response({'data': serializer.data, 'message':self.error_message.delete_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.delete_error_log(self, OBJECTO, id, ex))
            return Response({'message': self.error_message.delete_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class RenewalDateChaplainView(generics.UpdateAPIView):
    #queryset = m.Chaplain.objects.all()
    error_message = ErrorMessage
    serializer_class = RenewalDateChaplainSerializer
    permission_classes = [permissions.AllowAny]
    repository = ChaplainRepository()
    
    def update(self, request, id: int):
        OBJECTO = 'Capelão'
        try:
            
            chaplain = self.repository.get_chaplain(id)
            
            if not chaplain:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message': self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(chaplain, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_409_CONFLICT)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)

