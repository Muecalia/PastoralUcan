from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import SaveAgreementSerializer, ListAgreementSerializer, UpdateAgreementSerializer
from .models import Agreement
from utils.message_error import ErrorMessage
import logging


logger = logging.getLogger(__name__)

# Create your views here.

class AgreementRepository:
    def get_agreement(self, pk: int):
        try:
            return Agreement.objects.get(id=pk)
        except Agreement.DoesNotExist:
            return None


class SaveAgreementView(generics.CreateAPIView):
    #queryset = m.Agreement.objects.all()
    error_message = ErrorMessage
    serializer_class = SaveAgreementSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Convênio'
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


class ListAgreementView(generics.ListAPIView):
    queryset = Agreement.objects.all()
    serializer_class = ListAgreementSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Convênio'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindAgreementView(generics.ListAPIView):
    queryset = Agreement.objects.all()
    serializer_class = ListAgreementSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = AgreementRepository()
    
    def get(self, request, id: int, **kwargs):
        OBJECTO = 'Convênio'
        
        try:
            agreement = self.repository.get_agreement(id)
            
            if not agreement:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(agreement)
            logger.warning(self.error_message.list_success_log(self, OBJECTO, 1))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateAgreementView(generics.UpdateAPIView):
    error_message = ErrorMessage
    #queryset = Agreement.objects.all()
    serializer_class = UpdateAgreementSerializer
    permission_classes = [permissions.AllowAny]
    repository = AgreementRepository()
    
    def update(self, request, id: int, **kwargs):
        OBJECTO = 'Convênio'
        
        try:
            agreement = self.repository.get_agreement(id)
            
            if not agreement:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
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


class DeleteAgreementView(generics.DestroyAPIView):
    #queryset = Agreement.objects.all()
    serializer_class = ListAgreementSerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = AgreementRepository()
    
    def delete(self, request, id: int, **kwargs):
        OBJECTO = 'Convênio'
        
        try:
            agreement = self.repository.get_agreement(id)
            
            if not agreement:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(agreement)
            agreement.delete()
            logger.warning(self.error_message.delete_sucess_log(self, OBJECTO, id))
            return Response({'data': serializer.data, 'message':self.error_message.delete_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.delete_error_log(self, OBJECTO, id, ex))
            return Response({'message': self.error_message.delete_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


