from rest_framework.generics import CreateAPIView

from rest_framework.permissions import IsAuthenticated
from .serializers import FullApplicationCreateSerializer


class ApplicationCreateView(CreateAPIView):
    """APIview для создания заявки в базе."""
    serializer_class = FullApplicationCreateSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.data)
        return super().post(request)

