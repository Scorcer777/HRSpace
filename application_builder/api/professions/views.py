from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.professions.models import Profession

from .serializers import ProfessionSerializer


class ProfessionViewSet(viewsets.ReadOnlyModelViewSet):
    """Чтение списка/объекта 'Профессия'."""
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (IsAuthenticated,)
