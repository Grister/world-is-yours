from django_filters import rest_framework as filters
from order.models import Order


class OrderFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status')

    class Meta:
        model = Order
        fields = ['status']
