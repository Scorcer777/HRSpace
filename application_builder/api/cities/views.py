from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.cities.models import City

from .serializers import CitySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """Чтение списка/объекта 'Профессия'."""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)
