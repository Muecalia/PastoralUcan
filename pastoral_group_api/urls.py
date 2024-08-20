from django.contrib import admin
from django.urls import path
from .views import DeletePastoralGroupView, ListPastoralGroupView, FindPastoralGroupView, SavePastoralGroupView, UpdatePastoralGroupView

urlpatterns = [
    path('save_pastoral_group', SavePastoralGroupView.as_view(), name='save_pastoral_group'),
    path('list_pastoral_group', ListPastoralGroupView.as_view(), name='list_pastoral_group'),
    path('find_pastoral_group/<int:id>', FindPastoralGroupView.as_view(), name='find_pastoral_group'),
    path('delete_pastoral_group/<int:id>', DeletePastoralGroupView.as_view(), name='delete_pastoral_group'),
    path('update_pastoral_group/<int:id>', UpdatePastoralGroupView.as_view(), name='update_pastoral_group'),
]
