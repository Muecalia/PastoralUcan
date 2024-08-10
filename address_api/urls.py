from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('country', v.CountryView.as_view(), name='country'),
    path('province', v.ProvinceView.as_view(), name='province'),
    path('county', v.CountyView.as_view(), name='county'),
]
