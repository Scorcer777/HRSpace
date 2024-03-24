from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.cities.models import City

from .serializers import CitySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """Город."""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name',)
