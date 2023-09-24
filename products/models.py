from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    title = models.CharField(
        verbose_name='Название',
        unique=True,
        max_length=255
    )
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name='Владелец',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class AccessProduct(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='Пользователь с дотупом к продукту',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name='продукт, доступный пользователю',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user.username} имеет доступ к {self.product.title}'
