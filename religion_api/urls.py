from django.contrib import admin
from django.urls import path
from .views import CongregationView, ReligionView, SacramentView

urlpatterns = [
    path('congregation', CongregationView.as_view(), name='congregation'),
    path('religion', ReligionView.as_view(), name='religion'),
    path('sacrament', SacramentView.as_view(), name='sacrament'),
]
