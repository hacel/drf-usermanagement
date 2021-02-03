import django_filters
from django_filters.views import FilterView

from .models import URL


class URLFilter(django_filters.FilterSet):
    url = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = URL
        fields = ['url', 'action', 'comment']


class URLList(FilterView):
    model = URL
    filterset_class = URLFilter
    paginate_by = 15
