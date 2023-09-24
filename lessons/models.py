import cv2
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Lesson(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    video_path = models.FileField(
        upload_to='video/',
        verbose_name='ссылка на видео'
    )
    duration = models.PositiveIntegerField(
        verbose_name='длительность',
        blank=True,
        null=True,
    )
    product = models.ManyToManyField(
        'products.Product'
    )

    def __str__(self):
        return self.title


@receiver(post_save, sender=Lesson)
def calculate_video_duration(sender, instance, **kwargs):
    if not instance.duration:
        cap = cv2.VideoCapture(instance.video_path.path)

        if cap.isOpened():
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

            duration = frame_count / frame_rate

            instance.duration = duration
            instance.save()
            cap.release()


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
    view_time = models.PositiveIntegerField(
        verbose_name='Просмотрено'
    )
    viewed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.viewed = True if self.view_time >= 0.8 * self.lesson.duration else False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username + self.lesson.title
