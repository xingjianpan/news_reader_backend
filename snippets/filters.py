import django_filters
from .models import Snippet


class SnippetFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Snippet
        fields = ['title', 'description']
