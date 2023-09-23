import cv2
from django.contrib.auth import get_user_model
from django.db import models


class Lesson(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    video_path = models.FileField(
        verbose_name='ссылка на видео'
    )
    duration = models.DurationField(
        verbose_name='длительность',
    )

    def set_duration(self):
        cap = cv2.VideoCapture(self.video_path.path)

        if cap.isOpened():
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

            duration = frame_count / frame_rate

            cap.release()

            return duration

    def __str__(self):
        return self.title


class LessonView(models.Model):
    lesson = models.ForeignKey(
        'Lesson',
        verbose_name='Просматриваемый урок',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='Пользователь, просматривающий видео',
        on_delete=models.CASCADE
    )
    view_time = models.DurationField(
        verbose_name='Просмотрено'
    )
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.verbose_name, self.lesson.title
