from rest_framework import serializers

from products.models import Product


class ProductStatistics(serializers.ModelSerializer):
    product_title = serializers.CharField(source='title')
    lesson_view_count = serializers.IntegerField()
    total_view_duration = serializers.IntegerField()
    num_users = serializers.IntegerField()
    acquisition_percentage = serializers.FloatField()

    class Meta:
        model = Product
        fields = (
            'product_title',
            'lesson_view_count',
            'total_view_duration',
            'num_users',
            'acquisition_percentage',
        )
