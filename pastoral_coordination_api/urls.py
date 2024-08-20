from django.contrib import admin
from django.urls import path
from .views import DeletePastoralCoordinationView, FindPastoralCoordinationView, ListPastoralCoordinationView, SavePastoralCoordinationView, UpdatePastoralCoordinationView, RenewalDatePastoralCoordinationView

urlpatterns = [
    path('save_pastoral_coordination', SavePastoralCoordinationView.as_view(), name='save_pastoral_coordination'),
    path('list_pastoral_coordination', ListPastoralCoordinationView.as_view(), name='list_pastoral_coordination'),
    path('find_pastoral_coordination/<int:id>', FindPastoralCoordinationView.as_view(), name='find_pastoral_coordination'),
    path('delete_pastoral_coordination/<int:id>', DeletePastoralCoordinationView.as_view(), name='delete_pastoral_coordination'),
    path('update_pastoral_coordination/<int:id>', UpdatePastoralCoordinationView.as_view(), name='update_pastoral_coordination'),
    path('renewal_date_pastoral_coordination/<int:id>', RenewalDatePastoralCoordinationView.as_view(), name='renewal_date_pastoral_coordination'),
]
