from django.db import models

class Categories(models.Model):
    """
    Model Categories Dish
    """
    title_ru = models.CharField(
        max_length=100,
        verbose_name='Название категории на русском'
    )
    title_uz = models.CharField(
        max_length=100,
        verbose_name='Название категории на узбекском'
    )

    def __str__(self):
        return self.title_ru
    
    def __repr__(self):
        return f'Category: pk={self.pk}, title_ru={self.title_ru}, title_uz={self.title_uz}'
    
    class Meta:
        verbose_name = 'Категория Блюд'
        verbose_name_plural = 'Категории Блюд'
