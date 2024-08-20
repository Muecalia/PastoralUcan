from django.contrib import admin
from django.urls import path
from .views import DeleteChaplainView, FindChaplainView, ListChaplainView, SaveChaplainView, UpdateChaplainView, RenewalDateChaplainView

urlpatterns = [
    path('save_chaplain', SaveChaplainView.as_view(), name='save_chaplain'),
    path('list_chaplain', ListChaplainView.as_view(), name='list_chaplain'),
    path('find_chaplain/<int:id>', FindChaplainView.as_view(), name='find_chaplain'),
    path('delete_chaplain/<int:id>', DeleteChaplainView.as_view(), name='delete_chaplain'),
    path('update_chaplain/<int:id>', UpdateChaplainView.as_view(), name='update_chaplain'),
    path('renewal_date_chaplain/<int:id>', RenewalDateChaplainView.as_view(), name='renewal_date_chaplain'),
]
