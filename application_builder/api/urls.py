from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.industries.views import IndustryViewSet

app_name = 'api'
VERSION = 'v2'

router = DefaultRouter()
router.register('industries', IndustryViewSet, basename='industry')


urlpatterns = [
    path(f'{VERSION}/', include(router.urls)),
]
