from django.db import models
from Categories.models import Categories

from django.utils.safestring import mark_safe


class Dishes(models.Model):
    """
    Model Dishes
    """
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
         return super().__repr__()
    
    def descriptiontrim(self):
        return u"%s" % (self.description[:25],)
    
    descriptiontrim.allow_tags = True
    descriptiontrim.short_description = 'Описание'

    def img_preview(self): 
            return mark_safe(f'<img src="{self.image.url}" width="100px" height="75px"/>')
    
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    def get_category_title(self):
        return self.category.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'
