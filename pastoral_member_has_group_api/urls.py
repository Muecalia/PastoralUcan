from django.contrib import admin
from django.urls import path
from .views import DeletePastoralMemberHasGroupView, ListPastoralMemberHasGroupView, SavePastoralMemberHasGroupView, FindPastoralMemberHasGroupByGroupView, FindPastoralMemberHasGroupByMemberView

urlpatterns = [
    path('delete_pastoral_member_group', DeletePastoralMemberHasGroupView.as_view(), name='delete_pastoral_member_group'),
    path('list_pastoral_member_group', ListPastoralMemberHasGroupView.as_view(), name='list_pastoral_member_group'),
    path('save_pastoral_member_group', SavePastoralMemberHasGroupView.as_view(), name='save_pastoral_member_group'),
    path('find_pastoral_member_group_by_group/<int:group_id>', FindPastoralMemberHasGroupByGroupView.as_view(), name='find_pastoral_member_group_by_group'),
    path('find_pastoral_member_group_by_member/<int:member_id>', FindPastoralMemberHasGroupByMemberView.as_view(), name='find_pastoral_member_group_by_member'),
]
