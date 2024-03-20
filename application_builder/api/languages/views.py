from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.languages.models import Language

from .serializers import LanguageSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """Чтение списка/объекта язык."""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticated,)
