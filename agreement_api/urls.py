from django.contrib import admin
from django.urls import path
from .views import DeleteAgreementView, FindAgreementView, ListAgreementView, SaveAgreementView, UpdateAgreementView

urlpatterns = [
    path('save_agreement', SaveAgreementView.as_view(), name='save_agreement'),
    path('list_agreement', ListAgreementView.as_view(), name='list_agreement'),
    path('find_agreement/<int:id>', FindAgreementView.as_view(), name='find_agreement'),
    path('delete_agreement/<int:id>', DeleteAgreementView.as_view(), name='delete_agreement'),
    path('update_agreement/<int:id>', UpdateAgreementView.as_view(), name='update_agreement'),
]
