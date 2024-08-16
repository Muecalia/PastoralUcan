from django.contrib import admin
from django.urls import path
from .views import DeletePastoralActivityView, FindPastoralActivityView, ListPastoralActivityView, SavePastoralActivityView, UpdatePastoralActivityView

urlpatterns = [
    path('save_pastoral_activity', SavePastoralActivityView.as_view(), name='save_pastoral_activity'),
    path('list_pastoral_activity', ListPastoralActivityView.as_view(), name='list_pastoral_activity'),
    path('find_pastoral_activity/<int:id>', FindPastoralActivityView.as_view(), name='find_pastoral_activity'),
    path('delete_pastoral_activity/<int:id>', DeletePastoralActivityView.as_view(), name='delete_pastoral_activity'),
    path('update_pastoral_activity/<int:id>', UpdatePastoralActivityView.as_view(), name='update_pastoral_activity')
]
