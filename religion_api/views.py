from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import CongregationSerializer, ReligionSerializer, SacramentSerializer
from utils.message_error import ErrorMessage
from .models import Congregation, Religion, Sacrament
import logging


logger = logging.getLogger(__name__)


# Create your views here.
class CongregationView(generics.GenericAPIView):
    queryset = Congregation.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Congregação'
    serializer_class = CongregationSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request): 
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Congregação')}, status=status.HTTP_409_CONFLICT)
            
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.insert_success_log(self, self.OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.insert_success(self, self.OBJECTO)}, status=status.HTTP_201_CREATED)
            return Response({'message':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            logger.error(self.error_message.insert_error_log(self, self.OBJECTO, ex))
            return Response({'message': self.error_message.insert_error(self, self.OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)
        #else:
    
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, self.OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, self.OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, self.OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, self.OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)      


class ReligionView(generics.GenericAPIView):
    queryset = Religion.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Religião'
    serializer_class = ReligionSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Religião')}, status=status.HTTP_409_CONFLICT)
            
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.insert_success_log(self, self.OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.insert_success(self, self.OBJECTO)}, status=status.HTTP_201_CREATED)
            return Response({'message':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            logger.error(self.error_message.insert_error_log(self, self.OBJECTO, ex))
            return Response({'message': self.error_message.insert_error(self, self.OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, self.OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, self.OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, self.OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, self.OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)      


class SacramentView(generics.GenericAPIView):
    queryset = Sacrament.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Sacramento'
    serializer_class = SacramentSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Sacramento')}, status=status.HTTP_409_CONFLICT)
            
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.insert_success_log(self, self.OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.insert_success(self, self.OBJECTO)}, status=status.HTTP_201_CREATED)
            return Response({'message':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            logger.error(self.error_message.insert_error_log(self, self.OBJECTO, ex))
            return Response({'message': self.error_message.insert_error(self, self.OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, self.OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, self.OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, self.OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, self.OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)      


