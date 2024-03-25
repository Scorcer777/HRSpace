from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from apps.applications.models import Application

from .serializers import (FullApplicationCreateSerializer,
                          FullApplicationReadSerializer)
from .pagination import CustomPagination
from .filters import ApplicationFilter


class ApplicationListCreateView(ListCreateAPIView):
    """APIview для создания заявки в базе."""
    serializer_class = FullApplicationCreateSerializer
    permission_class = (IsAuthenticated,)
    queryset = Application.objects.all()
    pagination_class = CustomPagination
    filterset_class = ApplicationFilter
    ordering_fields = ('id')
    ordering = ('id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FullApplicationCreateSerializer
        return FullApplicationReadSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Заявка успешно создана!'},
                        status=status.HTTP_201_CREATED, headers=headers)


class ApplicationRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    """Вью для чтения / изменения одной заявки по ее id в URL."""
    serializer_class = FullApplicationReadSerializer
    permission_class = (IsAuthenticated,)
    allowed_methods = ['GET', 'PUT']

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return FullApplicationCreateSerializer
        return FullApplicationReadSerializer

    def get_queryset(self):
        return Application.objects.all()

    # Обновление данных для всех моделей.
    def update(self, request, pk):
        app_instance = self.get_object()
        serializer = self.get_serializer(app_instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Заявка успешно обновлена!'},
                        status=status.HTTP_200_OK)
