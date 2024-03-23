from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from apps.applications.models import (Application,
                                      JobInfo,
                                      CandidateRequirements,
                                      RecruitRequirements)
from apps.payments.models import Payment
from .serializers import (FullApplicationCreateSerializer,
                          FullApplicationReadSerializer,
                          ApplicationCreateSerializer,
                          JobInfoCreateSerializer,
                          CandidateRequirementsCreateSerializer,
                          RecruiterRequirementsCreateSerializer,
                          PaymentCreateSerializer)
from .pagination import CustomPagination
from .filters import ApplicationFilter


class ApplicationListCreateView(ListCreateAPIView):
    """APIview для создания заявки в базе."""
    serializer_class = FullApplicationCreateSerializer
    permission_class = (IsAuthenticated,)
    queryset = Application.objects.all()
    pagination_class = CustomPagination
    filter_class = ApplicationFilter
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
    # queryset = Application.objects.all()
    allowed_methods = ['GET', 'PUT', 'DELETE']

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ApplicationCreateSerializer
        return FullApplicationReadSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Application.objects.filter(id=pk)

    def update(self, request, pk):
        # Получение объекта модели по id из URL.
        app_instance = get_object_or_404(Application, id=pk)
        # Обновление данных для всех моделей.
        dict = {
            'application': {'model': Application,
                            'serializer': ApplicationCreateSerializer},
            'job_info': {'model': JobInfo,
                         'serializer': JobInfoCreateSerializer},
            'candidate_requirements': {
                'model': CandidateRequirements,
                'serializer': CandidateRequirementsCreateSerializer
            },
            'recruiter_requirements': {
                'model': RecruitRequirements,
                'serializer': RecruiterRequirementsCreateSerializer},
            'payments': {
                'model': Payment,
                'serializer': PaymentCreateSerializer
            }
        }
        for json_key, classes_dict in dict.items():
            if json_key == 'application':
                instance = app_instance
            else:
                instance = get_object_or_404(
                    classes_dict['model'], application=app_instance)
            serializer = classes_dict['serializer'](
                instance,
                data=request.data[json_key]
            )
            serializer.is_valid(raise_exception=True)
            serializer.update(
                instance,
                serializer.validated_data
            )
        return Response({'message': 'Заявка успешно обновлена!'},
                        status=status.HTTP_200_OK)
