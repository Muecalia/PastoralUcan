"""
URL configuration for pastoral_university project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Pastoral University",
        default_version='v1',),
    public=False,    
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/address/', include('address_api.urls'), name='address'),
    path('api/provider/', include('provider_api.urls'), name='provider'),
    path('api/agreement/', include('agreement_api.urls'), name='agreement'),
    path('api/religion/', include('religion_api.urls'), name='religion'),
    path('api/general/', include('general_api.urls'), name='general'),
    path('api/institution/', include('institution_api.urls'), name='institution'),
    #path('api/pastoral_member/', include('pastoral_member_api.urls'), name='pastoral_member'),
    path('api/agreement_project/', include('agreement_project_api.urls'), name='agreement_project'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]

