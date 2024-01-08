from django.db import models

from Users.models import UserProfile
from Dishes.models import Dishes

class Orders(models.Model):
    """
    Order of user
    """
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
    )
    dish = models.ForeignKey(
        Dishes,
        on_delete=models.CASCADE,
        verbose_name='Блюдо',
    )
    completed = models.BooleanField(
        verbose_name='Выполнен'
    )

    def __str__(self):
        return self.user.username
    
    def __repr__(self):
        return f'Order: pk={self.pk}, user={self.user}, dish={self.dish}, completed={self.completed}'
           
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    