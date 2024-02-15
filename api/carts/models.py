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
        verbose_name='Блюдо',
    )
    quantity = models.IntegerField(
        verbose_name='Колличество'
    )
    
    def get_dish_title(self):
        return self.dish.title
    
    def get_dish_price(self):
        return self.dish.price
    
    def get_dish_image(self):
        return self.dish.image
    
    def get_quantity(self):
        return self.quantity
    
    def __str__(self) -> str:
        return self.user.username

    def __repr__(self) -> str:
        return super().__repr__()

    @classmethod
    def update_or_create_cart_item(cls, user, dish, quantity):
        cart_item, created = cls.objects.get_or_create(
            user=user, 
            dish=dish, 
            quantity=quantity
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return cart_item

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
