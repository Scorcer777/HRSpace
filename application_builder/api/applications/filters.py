from django_filters import rest_framework as filters


class ApplicationFilter(filters.FilterSet):
    user = filters.CharFilter(field_name='user__email', lookup_expr='iexact')
    title = filters.CharFilter(lookup_expr='icontains')

    titleexact = filters.CharFilter(field_name='title', lookup_expr='iexact')
    profession = filters.CharFilter(
        field_name='profession__title',
        lookup_expr='icontains'
    )
    city = filters.CharFilter(
        field_name='city__name',
        lookup_expr='iexact'
    )
