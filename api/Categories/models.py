from django.db import models
from django.db.models import CharField


class Categories(models.Model):
    """
    Model Categories Dish
    """
    title_ru = models.CharField(
        max_length=100,
        verbose_name='Название категории RU'
    )
    
    title_uz = models.CharField(
        max_length=100,
        verbose_name='Название категории UZ'
    )
    
    def __str__(self) -> CharField:
        return self.title_ru

    def __repr__(self) -> str:
        return super().__repr__()

    class Meta:
        verbose_name = 'Категорию Блюда'
        verbose_name_plural = 'Категории Блюд'
