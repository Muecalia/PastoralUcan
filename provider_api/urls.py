from django.contrib import admin
from django.urls import path
from .views import DeleteProviderView, FindProviderView, ListProviderView, SaveProviderView, UpdateProviderView

urlpatterns = [
    path('save_provider', SaveProviderView.as_view(), name='save_provider'),
    path('list_provider', ListProviderView.as_view(), name='list_provider'),
    path('find_provider/<int:id>', FindProviderView.as_view(), name='find_provider'),
    path('delete_provider/<int:id>', DeleteProviderView.as_view(), name='delete_provider'),
    path('update_provider/<int:id>', UpdateProviderView.as_view(), name='update_provider')
]
