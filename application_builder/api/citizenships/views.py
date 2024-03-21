from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.citizenships.models import Citizenship

from .serializers import CitizenshipSerializer


class CitizenshipViewSet(viewsets.ReadOnlyModelViewSet):
    """Гражданство."""
    queryset = Citizenship.objects.all()
    serializer_class = CitizenshipSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('@name',)
    ordering_fields = ('name',)
