from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.industries.views import IndustryViewSet
from api.citizenships.views import CitizenshipViewSet
from api.professions.views import ProfessionSkillViewSet

app_name = 'api'
VERSION = 'v2'

router = DefaultRouter()
router.register('applications', IndustryViewSet, basename='application')
router.register('industries', IndustryViewSet, basename='industry')
router.register('citizenships', CitizenshipViewSet, basename='citizenship')


urlpatterns = [
    path(f'{VERSION}/', include(router.urls)),
]
