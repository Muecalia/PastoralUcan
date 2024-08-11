from django.contrib import admin
from django.urls import path
from .views import TypeInstitutionView

urlpatterns = [
    path('type_institution', TypeInstitutionView.as_view(), name='type_institution'),
    #path('list_provider', ListProviderView.as_view(), name='list_provider'),
    #path('find_provider/<int:id>', FindProviderView.as_view(), name='find_provider')
]
