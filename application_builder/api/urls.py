from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.industries.views import IndustryViewSet
from api.applications.views import ApplicationCreateView

app_name = 'api'
VERSION = 'v2'

router = DefaultRouter()
router.register('industries', IndustryViewSet, basename='industry')


urlpatterns = [
    path('applications/create/',
         ApplicationCreateView.as_view(),
         name='applications-create'),
    path(f'{VERSION}/', include(router.urls)),
]
