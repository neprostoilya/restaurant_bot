from django.db import models

class Categories(models.Model):
    """
    Model Categories Dish
    """
    title = models.CharField(
        max_length=100,
        verbose_name='Название категории'
    )

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    class Meta:
        verbose_name = 'Категорию Блюда'
        verbose_name_plural = 'Категории Блюд'
