from django.urls import path

from lessons import views

urlpatterns = [
    path('listlessonview/', views.LessonViewListAPIView.as_view(), name='ListLessonView'),
    path('listlesson/', views.ProductLessonListAPIView.as_view(), name='ListProductLesson')
]
