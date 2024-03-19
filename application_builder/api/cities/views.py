from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.cities.models import City

from .serializers import CitySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """Чтение списка/объекта City."""

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny]
