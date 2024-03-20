from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.applications.models import Application

from .serializers import ApplicationSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """Модель заявки."""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post', 'delete')
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
