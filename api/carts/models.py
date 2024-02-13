from django.db import models

from dishes.models import Dishes

from users.models import UserProfile


class Carts(models.Model):
    """
    Model Carts
    """
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    dish = models.ForeignKey(
        Dishes,
        on_delete=models.CASCADE,
        verbose_name='Блюдо'
    )
    amount = models.IntegerField(
        verbose_name='Колличество'
    )
    
    def __str__(self) -> str:
         return self.user.username

    def __repr__(self) -> str:
         return super().__repr__()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
