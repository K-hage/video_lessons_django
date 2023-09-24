from rest_framework import serializers

from lessons.models import LessonView, Lesson


class LessonViewListSerializer(serializers.ModelSerializer):
    lesson = serializers.SlugRelatedField(
        queryset=Lesson.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = LessonView
        fields = ('lesson', 'viewed', 'view_time')
