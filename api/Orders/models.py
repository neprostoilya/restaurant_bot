from django.db import models

from users.models import UserProfile
from dishes.models import Dishes
from places.models import Places

class Orders(models.Model):
    """
    Order of user
    """
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
    )
    place = models.ForeignKey(
        Places,
        on_delete=models.CASCADE,
        verbose_name='Место'
    )
    people_quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Кол-во людей'
    )
    datetime_created = models.DateTimeField(
        auto_now=True,
        verbose_name='Время создания'
    )
    datetime_selected = models.TimeField(
        verbose_name='Указанное время'
    )
    status = models.CharField(
        verbose_name='Статус'
    )
    
    def total_price_all_dishes(self):
        dishes_order: dict = DishOrder.objects.filter(
            order_id=self.pk
        )
        
        total_price: int = 0
        
        for dish in dishes_order:
            total_price += dish.total_price
        
        return total_price
    
    total_price_all_dishes.allow_tags = True
    total_price_all_dishes.short_description = 'Общая цена'

    def total_quantity_all_dishes(self):
        dishes_order: dict = DishOrder.objects.filter(
            order_id=self.pk
        )
        
        total_quantity: int = 0
        
        for dish in dishes_order:
            total_quantity += dish.total_quantity
        
        return total_quantity
    
    total_quantity_all_dishes.allow_tags = True
    total_quantity_all_dishes.short_description = 'Общее кол-во'

    def __str__(self) -> str:
        return self.user.username
    
    def __repr__(self) -> str:
        return super().__repr__()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



class DishOrder(models.Model):
    """
    Order dish
    """
    order = models.ForeignKey(
        Orders,
        verbose_name='Заказ',
        on_delete=models.CASCADE
    )
    dish = models.ForeignKey(
        Dishes,
        verbose_name='Блюдо',
        on_delete=models.CASCADE
    )
    total_price = models.PositiveIntegerField(
        default=0,
        verbose_name='Общая стоимость'
    )
    total_quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Общее кол-во'
    )
    
    def __str__(self) -> str:
        return self.order.user.username
    
    def __repr__(self) -> str:
        return super().__repr__()

    class Meta:
        verbose_name = 'Заказанное блюдо'
        verbose_name_plural = 'Заказанные блюда'
