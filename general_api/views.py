from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import AcademicLevelSerializer, TypeActivitySerializer, SchoolSerializer, UniversitySerializer
from .models import AcademicLevel, TypeActivity, School, University
from utils.message_error import ErrorMessage
import logging

logger = logging.getLogger(__name__)


# Create your views here.
class AcademicLevelView(generics.GenericAPIView):
    queryset = AcademicLevel.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Nível académico'
    serializer_class = AcademicLevelSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Nível académico')}, status=status.HTTP_409_CONFLICT)
            
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


class TypeActivityView(generics.GenericAPIView):
    queryset = TypeActivity.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Tipo Actividade'
    serializer_class = TypeActivitySerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
           
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Tipo Actividade')}, status=status.HTTP_409_CONFLICT)
            
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


class SchoolLevelView(generics.GenericAPIView):
    queryset = School.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Escola'
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Escola')}, status=status.HTTP_409_CONFLICT)
            
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


class UniversityView(generics.GenericAPIView):
    queryset = University.objects.all()
    error_message = ErrorMessage
    OBJECTO = 'Universidade'
    serializer_class = UniversitySerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        try:
            if self.queryset.filter(name=request.data['name']).exists():
                return Response({'message':self.error_message.exists(self, 'Universidade')}, status=status.HTTP_409_CONFLICT)
            
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
        
