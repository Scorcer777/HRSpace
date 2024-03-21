from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.professions.models import Profession

from .serializers import ProfessionSerializer


class ProfessionViewSet(viewsets.ReadOnlyModelViewSet):
    """Профессия."""
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('@title',)
    ordering_fields = ('title',)
