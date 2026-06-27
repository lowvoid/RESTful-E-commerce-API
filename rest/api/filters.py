import django_filters
from rest_framework import filters

from api.models import Product, Order


class InStockFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        in_stock = request.query_params.get('in_stock')
        if in_stock is not None:
            if in_stock.lower() == 'true':
                return queryset.filter(stock__gt=0)
            elif in_stock.lower() == 'false':
                return queryset.filter(stock__lte=0)
        return queryset


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['iexact', 'icontains'],
            'price': ['exact', 'gte', 'lte', 'gt', 'lt', 'range'],
        }


class OrderFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at__date')

    class Meta:
        model = Order
        fields = {
            'status': ['exact'],
            'created_at': ['exact', 'gt', 'lt'],
        }
