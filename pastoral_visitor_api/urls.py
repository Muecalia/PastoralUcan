from django.contrib import admin
from django.urls import path
from .views import DeletePastoralVisitorView, FindPastoralVisitorView, ListPastoralVisitorView, SavePastoralVisitorView

urlpatterns = [
    path('save_pastoral_visitor', SavePastoralVisitorView.as_view(), name='save_pastoral_visitor'),
    path('list_pastoral_visitor', ListPastoralVisitorView.as_view(), name='list_pastoral_visitor'),
    path('find_pastoral_visitor/<int:id>', FindPastoralVisitorView.as_view(), name='find_pastoral_visitor'),
    path('delete_pastoral_visitor/<int:id>', DeletePastoralVisitorView.as_view(), name='delete_pastoral_visitor')
    #path('update_pastoral_visitor/<int:id>', UpdatePastoralVisitorView.as_view(), name='update_pastoral_visitor')
]
