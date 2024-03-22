import django_filters

from apps.applications.models import Application


def get_start_w_queryset(request):
    if request is None:
        return Application.objects.none()
    return Application.filter(
        start_working=request.GET.get('start_working')
    )


class ApplicationFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    title__ex = django_filters.CharFilter(lookup_expr='iexact')
    profession = django_filters.CharFilter(
        field_name='profession__title',
        lookup_expr='icontains'
    )
    min_salary__gt = django_filters.NumberFilter(
        field_name='min_salary',
        lookup_expr='gt'
    )
    max_salary__gt = django_filters.NumberFilter(
        field_name='max_salary',
        lookup_expr='gt'
    )
    min_salary__gt = django_filters.NumberFilter(
        field_name='min_salary',
        lookup_expr='lt'
    )
    max_salary__gt = django_filters.NumberFilter(
        field_name='max_salary',
        lookup_expr='lt'
    )
    id = django_filters.NumberFilter(
        field_name='id',
        lookup_expr='iexact'
    )
    city = django_filters.CharFilter(
        field_name='city__name',
        lookup_expr='iexact'
    )
    start_working = django_filters.ModelChoiceFilter(
        queryset=get_start_w_queryset
    )

    class Meta:
        model = Application
        fields = [
            'title',
            'profession',
            'city',
            'id',
            'min_salary',
            'max_salary',
            'start_working',
        ]
