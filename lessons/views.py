from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from lessons.filters import ProductLessonViewFilter
from lessons.models import LessonView
from lessons.serializers import LessonViewListSerializer, ProductLessonListSerializer
from products.models import AccessProduct


class LessonViewListAPIView(ListAPIView):
    serializer_class = LessonViewListSerializer

    def get_queryset(self):
        user = self.request.user

        accessible_products = AccessProduct.objects.filter(user=user).values_list('product_id', flat=True)

        queryset = LessonView.objects.filter(lesson__product__in=accessible_products)

        return queryset


class ProductLessonListAPIView(ListAPIView):
    serializer_class = ProductLessonListSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = ProductLessonViewFilter

    def get_queryset(self):
        user = self.request.user

        accessible_products = AccessProduct.objects.filter(user=user).values_list('product_id', flat=True)

        queryset = LessonView.objects.filter(lesson__product__in=accessible_products)

        return queryset
