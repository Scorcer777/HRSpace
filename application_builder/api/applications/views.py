from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import FullApplicationCreateSerializer


class ApplicationCreateView(CreateAPIView):
    """APIview для создания заявки в базе."""
    serializer_class = FullApplicationCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Заявка успешно создана!'},
                        status=status.HTTP_201_CREATED, headers=headers)
