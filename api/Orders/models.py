from django.db import models

from users.models import UserProfile
from dishes.models import Dishes


status = (('Ожидание', 'Ожидание'), ('Принят', 'Принят'), ('Закончен', 'Закончен'))


class Orders(models.Model):
    """
    Order of user
    """
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
    )
    dishes = models.ManyToManyField(
        Dishes,
        verbose_name='Блюда'
    )
    table = models.IntegerField(
        verbose_name='Номер стола'
    )
    people_quantity = models.IntegerField(
        default=1,
        verbose_name='Кол-во людей'
    )
    total_price = models.IntegerField(
        default=0,
        verbose_name='Общая стоимость'
    )
    total_quantity = models.IntegerField(
        default=0,
        verbose_name='Общее кол-во'
    )
    datetime_created = models.DateTimeField(
        auto_now=True,
        verbose_name='Время создания'
    )
    datetime_selected = models.TimeField(
        verbose_name='Указанное время'
    )
    status = models.CharField(
        choices=status,
    )
    
    def __str__(self) -> str:
        return self.user.username
    
    def __repr__(self) -> str:
        return super().__repr__()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
