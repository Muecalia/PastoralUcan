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
    path('api/general/', include('general_api.urls'), name='general'),
    path('api/address/', include('address_api.urls'), name='address'),
    path('api/provider/', include('provider_api.urls'), name='provider'),
    path('api/religion/', include('religion_api.urls'), name='religion'),    
    path('api/chaplain/', include('chaplain_api.urls'), name='chaplain'),
    path('api/agreement/', include('agreement_api.urls'), name='agreement'),
    path('api/publication/', include('publication_api.urls'), name='publication'),
    path('api/institution/', include('institution_api.urls'), name='institution'),
    path('api/pastoral_group/', include('pastoral_group_api.urls'), name='pastoral_group'),
    path('api/pastoral_member/', include('pastoral_member_api.urls'), name='pastoral_member'),
    path('api/pastoral_visitor/', include('pastoral_visitor_api.urls'), name='pastoral_visitor'),
    path('api/pastoral_activity/', include('pastoral_activity_api.urls'), name='pastoral_activity'),
    path('api/agreement_project/', include('agreement_project_api.urls'), name='agreement_project'),
    path('api/pastoral_coordination/', include('pastoral_coordination_api.urls'), name='pastoral_coordination'),
    path('api/pastoral_member_group/', include('pastoral_member_has_group_api.urls'), name='pastoral_member_group'),
    path('api/pastoral_activity_member/', include('pastoral_activity_member_api.urls'), name='pastoral_activity_member'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]

