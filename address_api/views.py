from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import CountrySerializer, CountySerializer, ProvinceSerializer
from .models import Country, County, Province
from utils.message_error import ErrorMessage
import logging

logger = logging.getLogger(__name__)


# Create your views here.
class CountryView(generics.GenericAPIView):
    queryset = Country.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'País'
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'País')}, status=status.HTTP_409_CONFLICT)
            
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


class CountyView(generics.GenericAPIView):
    queryset = County.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Município'
    serializer_class = CountySerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
           
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Município')}, status=status.HTTP_409_CONFLICT)
            if not Province.objects.filter(id=request.data['province']).exists():
                return Response({'message':self.error_message.not_found(self, 'Provincia')}, status=status.HTTP_404_NOT_FOUND)
            
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
        

class ProvinceView(generics.GenericAPIView):
    queryset = Province.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Província'
    serializer_class = ProvinceSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Provincia')}, status=status.HTTP_409_CONFLICT)
            if not Country.objects.filter(id=request.data['country']).exists():
                return Response({'message':self.error_message.not_found(self, 'País')}, status=status.HTTP_404_NOT_FOUND)
            
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
