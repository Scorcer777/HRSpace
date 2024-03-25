from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="HRSpace",
      default_version='v2',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path(
       'api/swagger<format>/',
       schema_view.without_ui(cache_timeout=0),
       name='schema-json'
    ),
   path(
       'api/swagger/',
       schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'
    ),
   path(
       'api/redoc/',
       schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'
    ),
]
