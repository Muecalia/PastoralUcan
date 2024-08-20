from django.contrib import admin
from django.urls import path
from .views import DeletePastoralMemberView, FindPastoralMemberView, ListPastoralMemberView, SavePastoralMemberView, UpdatePastoralMemberView

urlpatterns = [
    path('save_pastoral_member', SavePastoralMemberView.as_view(), name='save_pastoral_member'),
    path('list_pastoral_member', ListPastoralMemberView.as_view(), name='list_pastoral_member'),
    path('find_pastoral_member/<int:id>', FindPastoralMemberView.as_view(), name='find_pastoral_member'),
    path('delete_pastoral_member/<int:id>', DeletePastoralMemberView.as_view(), name='delete_pastoral_member'),
    path('update_pastoral_member/<int:id>', UpdatePastoralMemberView.as_view(), name='update_pastoral_member')
]
