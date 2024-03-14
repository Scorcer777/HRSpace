from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.industries.models import Industry

from .serializers import IndustrySerializer


class IndustryViewSet(viewsets.ReadOnlyModelViewSet):
    """Чтение списка/объекта отрасль."""
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [AllowAny]
    pagination_class = None
