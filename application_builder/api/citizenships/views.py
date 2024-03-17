from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.citizenships.models import Citizenship

from .serializers import CitizenshipSerializer


class CitizenshipViewSet(viewsets.ReadOnlyModelViewSet):
    """Гражданство."""
    queryset = Citizenship.objects.all()
    serializer_class = CitizenshipSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
