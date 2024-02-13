from django.db import models

from dishes.models import Dishes


class Orders(models.Model):
    """
    Order of user
    """
    name = models.CharField(
        verbose_name='Имя'
    )
    surname = models.CharField(
        verbose_name='Фамилия'
    )
    phone = models.CharField(
        verbose_name='Номер'
    )
    dish = models.ForeignKey(
        Dishes,
        on_delete=models.CASCADE,
        verbose_name='Блюдо',
    )
    datetime = models.DateTimeField(
        verbose_name='Дата'
    )

    def __str__(self) -> str:
        return self.dish.title

    def __repr__(self) -> str:
        return super().__repr__()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
