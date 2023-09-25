from django.urls import path

from products import views

urlpatterns = [
    path('productstatistics/', views.ProductStatisticsView.as_view(), name='ProductStatistic'),
]
