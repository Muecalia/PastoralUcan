from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import FindPastoralActivitySerializer, ListPastoralActivitySerializer, SavePastoralActivitySerializer, UpdatePastoralActivitySerializer, UpdatePastoralActivityStatusSerializer
from .models import TypeActivity, PastoralActivity
from publication_api.models import Publication
from pastoral_activity_member_api.models import PastoralActivityMember
from utils.message_error import ErrorMessage
import logging


logger = logging.getLogger(__name__)

# Create your views here.

class PastoralActivityRepository:
    def get_pastoral_activity(self, pk: int):
        try:
            return PastoralActivity.objects.get(id=pk)
        except PastoralActivity.DoesNotExist:
            return None


class SavePastoralActivityView(generics.CreateAPIView):
    #queryset = m.PastoralActivity.objects.all()
    error_message = ErrorMessage
    serializer_class = SavePastoralActivitySerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        OBJECTO = 'Actividade da Pastoral'
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


class ListPastoralActivityView(generics.ListAPIView):
    queryset = PastoralActivity.objects.all()
    serializer_class = ListPastoralActivitySerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    
    def get(self, request, *args, **kwargs):
        OBJECTO = 'Actividade da Pastoral'
        try:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            logger.info(self.error_message.list_success_log(self, OBJECTO, len(self.queryset.all())))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class FindPastoralActivityView(generics.RetrieveAPIView):
    queryset = PastoralActivity.objects.all()
    serializer_class = FindPastoralActivitySerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = PastoralActivityRepository()
    
    def get(self, request, id: int):
        OBJECTO = 'Actividade da Pastoral'
        try:
            pastoral_activity = self.repository.get_pastoral_activity(id)
            
            if not pastoral_activity:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(pastoral_activity)
            logger.info(self.error_message.list_success_log(self, OBJECTO, 1))
            return Response({'data': serializer.data, 'message':self.error_message.list_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.list_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.list_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePastoralActivityView(generics.UpdateAPIView):
    #queryset = m.PastoralActivity.objects.all()
    error_message = ErrorMessage
    serializer_class = UpdatePastoralActivitySerializer
    permission_classes = [permissions.AllowAny]
    repository = PastoralActivityRepository()
    
    def update(self, request, id: int):
        OBJECTO = 'Actividade da Pastoral'
        try:
            
            pastoral_activity = self.repository.get_pastoral_activity(id)
            
            if not pastoral_activity:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message': self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(pastoral_activity, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_409_CONFLICT)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePastoralActivityStatusView(generics.UpdateAPIView):
    #queryset = m.PastoralActivity.objects.all()
    error_message = ErrorMessage
    serializer_class = UpdatePastoralActivityStatusSerializer
    permission_classes = [permissions.AllowAny]
    repository = PastoralActivityRepository()
    
    def update(self, request, id: int):
        OBJECTO = 'Actividade da Pastoral'
        try:
            
            pastoral_activity = self.repository.get_pastoral_activity(id)
            
            if not pastoral_activity:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message': self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(pastoral_activity, data=request.data, partial=True)
            #serializer = self.serializer_class(pastoral_activity, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(self.error_message.update_success_log(self, OBJECTO))
                return Response({'data': serializer.data, 'message':self.error_message.update_success(self, OBJECTO)}, status=status.HTTP_200_OK)
            return Response({'message':serializer.errors}, status=status.HTTP_409_CONFLICT)
        except Exception as ex:
            logger.error(self.error_message.update_error_log(self, OBJECTO, ex))
            return Response({'message': self.error_message.update_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)


class DeletePastoralActivityView(generics.DestroyAPIView):
    #queryset = PastoralActivity.objects.all()
    serializer_class = ListPastoralActivitySerializer
    permission_classes = [permissions.AllowAny]
    error_message = ErrorMessage
    repository = PastoralActivityRepository()
    
    def delete(self, request, id: int, **kwargs):
        OBJECTO = 'Actividade da Pastoral'
        
        try:
            pastoral_activity = self.repository.get_pastoral_activity(id)
            
            if not pastoral_activity:
                logger.warning(self.error_message.not_found_log(self, OBJECTO, id))
                return Response({'message':self.error_message.not_found(self, OBJECTO)}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(pastoral_activity)
            
            pastoral_activity_member = PastoralActivityMember.objects.filter(pastoral_activity=pastoral_activity)
            
            if len(pastoral_activity_member) > 0:
                logger.warning(self.error_message.activity_error_log(self, OBJECTO, len(pastoral_activity_member)))
                return Response({'data': serializer.data, 'message':self.error_message.activity_error(self, OBJECTO)}, status=status.HTTP_200_OK)
            
            try:
                publication = Publication.objects.get(pastoral_activity=pastoral_activity)
                publication.delete()
            except Publication.DoesNotExist:
                print('Publicação não encontrada')
            
            pastoral_activity.delete()
            logger.warning(self.error_message.delete_sucess_log(self, OBJECTO, id))
            return Response({'data': serializer.data, 'message':self.error_message.delete_success(self, OBJECTO)}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(self.error_message.delete_error_log(self, OBJECTO, id, ex))
            return Response({'message': self.error_message.delete_error(self, OBJECTO)}, status=status.HTTP_400_BAD_REQUEST)

