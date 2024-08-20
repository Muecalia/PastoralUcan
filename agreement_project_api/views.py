from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import ChangeStateProjectSerializer, SaveAgreementProjectSerializer, ListAgreementProjectSerializer, UpdateAgreementProjectSerializer
from .models import AgreementProject
from utils.message_error import ErrorMessage
import logging


logger = logging.getLogger(__name__)

# Create your views here.

class AgreementProjectRepository:
    def get_agreement(self, pk: int):
        try:
            return AgreementProject.objects.get(id=pk)
        except AgreementProject.DoesNotExist:
            return None


class SaveAgreementProjectView(generics.CreateAPIView):
    #queryset = m.AgreementProject.objects.all()
    error_message = ErrorMessage
    serializer_class = SaveAgreementProjectSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Convênio Projecto'
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


class ListAgreementProjectView(generics.ListAPIView):
    queryset = AgreementProject.objects.all()
    serializer_class = ListAgreementProjectSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Convênio Projecto'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindAgreementProjectView(generics.ListAPIView):
    queryset = AgreementProject.objects.all()
    serializer_class = ListAgreementProjectSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = AgreementProjectRepository()
    
    def get(self, request, id: int, **kwargs):
        OBJECTO = 'Convênio Projecto'
        
        try:
            agreement = self.repository.get_agreement(id)
            
            if not agreement:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(agreement)
            logger.warning(self.error_message.list_success_log(self, OBJECTO, 1))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateAgreementProjectView(generics.UpdateAPIView):
    error_message = ErrorMessage
    queryset = AgreementProject.objects.all()
    serializer_class = UpdateAgreementProjectSerializer
    permission_classes = [permissions.AllowAny]
    repository = AgreementProjectRepository()
    
    def update(self, request, id: int, **kwargs):
        OBJECTO = 'Convênio Projecto'
        
        try:
            agreement = self.repository.get_agreement(id)
            
            if not agreement:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)   
        
            serializer = self.serializer_class(agreement, data=request.data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class ChangeStateProjectView(generics.UpdateAPIView):
    error_message = ErrorMessage
    queryset = AgreementProject.objects.all()
    serializer_class = ChangeStateProjectSerializer
    permission_classes = [permissions.AllowAny]
    repository = AgreementProjectRepository()
    
    def update(self, request, id: int, **kwargs):
        OBJECTO = 'State Project'
        
        try:
            agreement = self.repository.get_agreement(id)
            
            if not agreement:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)   
        
            serializer = self.serializer_class(agreement, data=request.data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)
        

class DeleteAgreementProjectView(generics.DestroyAPIView):
    queryset = AgreementProject.objects.all()
    serializer_class = ListAgreementProjectSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = AgreementProjectRepository()
    
    def delete(self, request, id: int, **kwargs):
        OBJECTO = 'Convênio Projecto'
        
        try:
            agreement = self.repository.get_agreement(id)
            
            if not agreement:
                logger.info(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(agreement)
            agreement.delete()
            logger.warning(self.error_message.delete_sucess_log(self, OBJECTO, id))
            return Response({'data': serializer.data, 'message':self.error_message.delete_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.delete_error_log(self, OBJECTO, id, ex))
            return Response({'message': self.error_message.delete_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


