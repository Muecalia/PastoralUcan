from django.contrib import admin
from django.urls import path
from .views import FindPastoralActivityMemberView, ListPastoralActivityMemberView, SavePastoralActivityMemberView, SavePastoralActivityVisitorView, UpdatePastoralActivityMemberView

urlpatterns = [
    path('save_pastoral_activity_member', SavePastoralActivityMemberView.as_view(), name='save_pastoral_activity_member'),
    path('save_pastoral_activity_visitor', SavePastoralActivityVisitorView.as_view(), name='save_pastoral_activity_visitor'),
    path('list_pastoral_activity_member', ListPastoralActivityMemberView.as_view(), name='list_pastoral_activity_member'),
    path('find_pastoral_activity_member/<int:id>', FindPastoralActivityMemberView.as_view(), name='find_pastoral_activity_member'),
    #path('delete_pastoral_activity_member/<int:id>', DeletePastoralActivityView.as_view(), name='delete_pastoral_activity_member'),
    path('update_pastoral_activity_member/<int:id>', UpdatePastoralActivityMemberView.as_view(), name='update_pastoral_activity_member')
]
