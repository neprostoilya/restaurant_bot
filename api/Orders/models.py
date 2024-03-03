from django.db import models

from users.models import UserProfile


class Orders(models.Model):
    """
    Order of user
    """
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
    )
    table = models.IntegerField(
        verbose_name='Номер стола'
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
    datetime_selected = models.DateTimeField(
        verbose_name='Указанное время'
    )
    
    def __str__(self) -> str:
        return self.user.username
    
    def __repr__(self) -> str:
        return super().__repr__()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
