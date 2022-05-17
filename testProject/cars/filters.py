from cars.models import Car
from django_filters.rest_framework import (
    FilterSet, BooleanFilter,
    NumberFilter
)


class CarFilters(FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    question_4 = BooleanFilter(field_name="question_4", label='question_4')
    question_6 = BooleanFilter(field_name="question_6", label='question_6')
    owner_age = NumberFilter(field_name='owner_age', label='owner_age')

    class Meta:
        model = Car
        fields = ['color', 'type', 'length']
