from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.applications.models import Application
from .serializers import (FullApplicationCreateSerializer,
                          FullApplicationReadSerializer)
from .pagination import CustomPagination
from .filters import ApplicationFilter


class ApplicationCreateView(CreateAPIView):
    """APIview для создания заявки в базе."""
    serializer_class = FullApplicationCreateSerializer
    # permission_class = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Заявка успешно создана!'},
                        status=status.HTTP_201_CREATED, headers=headers)


class ApplicationListView(ListAPIView):
    """
    Вью для просмотра списка заявок.
    Возможна фильтрация с помощью query params.
    """
    serializer_class = FullApplicationReadSerializer
    # permission_class = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    queryset = Application.objects.all()
    pagination_class = CustomPagination
    filter_class = ApplicationFilter
    ordering_fields = ('id')
    ordering = ('id')


class ApplicationDetailView(RetrieveAPIView):
    """Вью для чтения одной заявки основываясь по id в URL."""
    serializer_class = FullApplicationReadSerializer
    permission_class = (IsAuthenticated,)
    queryset = Application.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Application.objects.filter(id=pk)
