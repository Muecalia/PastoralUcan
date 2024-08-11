from django.contrib import admin
from django.urls import path
from .views import ChangeStateProjectView, DeleteAgreementProjectView, FindAgreementProjectView, ListAgreementProjectView, SaveAgreementProjectView, UpdateAgreementProjectView

urlpatterns = [
    path('save_agreement_project', SaveAgreementProjectView.as_view(), name='save_agreement_project'),
    path('list_agreement_project', ListAgreementProjectView.as_view(), name='list_agreement_project'),
    path('change_state_project/<int:id>', ChangeStateProjectView.as_view(), name='change_state_project'),
    path('find_agreement_project/<int:id>', FindAgreementProjectView.as_view(), name='find_agreement_project'),
    path('delete_agreement_project/<int:id>', DeleteAgreementProjectView.as_view(), name='delete_agreement_project'),
    path('update_agreement_project/<int:id>', UpdateAgreementProjectView.as_view(), name='update_agreement_project')
]
