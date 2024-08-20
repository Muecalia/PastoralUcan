from django.contrib import admin
from django.urls import path
from .views import DeletePublicationView, FindPublicationView, ListPublicationView, SavePublicationView, UpdatePublicationView

urlpatterns = [
    path('save_publication', SavePublicationView.as_view(), name='save_publication'),
    path('list_publication', ListPublicationView.as_view(), name='list_publication'),
    path('find_publication/<int:id>', FindPublicationView.as_view(), name='find_publication'),
    path('delete_publication/<int:id>', DeletePublicationView.as_view(), name='delete_publication'),
    path('update_publication/<int:id>', UpdatePublicationView.as_view(), name='update_publication'),
]
