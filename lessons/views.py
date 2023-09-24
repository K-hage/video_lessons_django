from rest_framework.generics import ListAPIView

from lessons.models import LessonView
from lessons.serializers import LessonViewListSerializer
from products.models import AccessProduct


class LessonViewListAPIView(ListAPIView):
    queryset = LessonView.objects.all()
    serializer_class = LessonViewListSerializer

    def get_queryset(self):
        user = self.request.user

        accessible_products = AccessProduct.objects.filter(user=user).values_list('product_id', flat=True)

        queryset = LessonView.objects.filter(lesson__product__in=accessible_products)

        return queryset
