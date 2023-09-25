import django_filters
from django.db import models
from django_filters import IsoDateTimeFilter

from lessons.models import LessonView


class ProductLessonViewFilter(django_filters.FilterSet):
    product_title = django_filters.CharFilter(field_name='lesson__product__title', lookup_expr='exact')

    class Meta:
        model = LessonView
        fields = (
            'product_title',
        )

        filter_overrides = {
            models.DateTimeField: {'filter_class': IsoDateTimeFilter},
        }
