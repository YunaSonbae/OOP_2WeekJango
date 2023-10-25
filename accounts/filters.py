import django_filters
from .models import Application


class CategoryFilters(django_filters.FilterSet):
    class Meta:
        model = Application
        exclude = ['img']
        fields = ['category']
