from django.db import models
from categories.models import Categories

from django.utils.safestring import mark_safe


class Dishes(models.Model):
    """
    Model Dishes
    """
    jovy_dish_pk = models.IntegerField(
        verbose_name='Айди блюда в Jovy'
    )
    image = models.ImageField(
        upload_to='dishes/', 
        verbose_name='Изображение'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Название блюда'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    
    category = models.ForeignKey(
        Categories, 
        on_delete=models.CASCADE, 
        verbose_name='Категория',
        related_name='category'
    )
    price = models.PositiveBigIntegerField(
        verbose_name='Цена',
        default=0
    )

    def __str__(self) -> str:
         return self.title

    def __repr__(self) -> str:
         return (f'Dishes: image={self.image}, title={self.title}, description={self.description},'
                 f' category={self.category}, pric{self.price}')
    
    def descriptiontrim(self):
        return u"%s" % (self.description[:35],) + '...'
    
    descriptiontrim.allow_tags = True
    descriptiontrim.short_description = 'Описание'

    def img_preview(self): 
            return mark_safe(f'<img src="{self.image.url}" width="100px" height="100px"/>')
    
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    def get_category_title(self):
        return self.category.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'
