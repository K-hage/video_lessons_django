from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework.generics import ListAPIView

from lessons.models import LessonView
from products.models import Product, AccessProduct
from products.serializers import ProductStatistics


class ProductStatisticsView(ListAPIView):
    serializer_class = ProductStatistics

    def get_queryset(self):
        products = Product.objects.all()
        product_stats = []

        for product in products:
            lesson_view_count = (
                LessonView.objects.
                select_related('Lesson', 'Product').
                filter(lesson__product=product, viewed=True).count()
            )
            total_view_duration = (
                LessonView.objects.
                filter(lesson__product=product).
                aggregate(total_duration=Sum('view_time'))['total_duration']
            )
            num_users = AccessProduct.objects.filter(product=product).count()
            total_users_count = get_user_model().objects.count()

            acquisition_percentage = (num_users / total_users_count) * 100 if total_users_count > 0 else 0

            stats = {
                'title': product.title,
                'lesson_view_count': lesson_view_count,
                'total_view_duration': total_view_duration,
                'num_users': num_users,
                'acquisition_percentage': acquisition_percentage,
            }

            product_stats.append(stats)

        return product_stats
