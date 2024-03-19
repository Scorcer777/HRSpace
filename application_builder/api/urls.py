from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.industries.views import IndustryViewSet
from api.cities.views import CityViewSet


app_name = 'api'
VERSION = 'v2'

router = DefaultRouter()
router.register('industries', IndustryViewSet, basename='industry')
router.register('cities', CityViewSet, basename='city')


urlpatterns = [
    path(f'{VERSION}/', include(router.urls)),
]
