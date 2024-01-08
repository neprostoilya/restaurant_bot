from django.db import models
from Categories.models import Categories

from django.utils.safestring import mark_safe

class Dishes(models.Model):
    """
    Model Dishes
    """
    title_ru = models.CharField(
        max_length=155,
        verbose_name='Название блюда на русском'
    )
    title_uz = models.CharField(
        max_length=155,
        verbose_name='Название блюда на узбекском'
    )
    image = models.ImageField(
        upload_to='dishes/', 
        null=True, 
        blank=True, 
        verbose_name='Изображение'
    )
    description_ru = models.TextField(
        verbose_name='Описание на русском'
    )
    description_uz = models.TextField(
        verbose_name='Описание на узбекском'
    )
    category = models.ForeignKey(
        Categories, 
        on_delete=models.CASCADE, 
        verbose_name='Категория',
        related_name='category'
    )
    price = models.IntegerField(
        verbose_name='Цена',
        default=0
    )

    def __str__(self) -> str:
         return self.title_ru

    def __repr__(self):
        return f'Dish: pk={self.pk}, title_ru={self.title_ru}, title_uz={self.title_uz}, image={self.image}, \
        description_ru={self.description_ru}, description_uz={self.description_uz}, category={self.category}'
    
    def descriptiontrim(self):
        return u"%s..." % (self.description_ru[:25],)
    
    descriptiontrim.allow_tags = True
    descriptiontrim.short_description = 'Описание'

    def img_preview(self): 
            return mark_safe(f'<img src="{self.image.url}" width="75px" height="75px"/>')
    
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    def get_category_title_ru(self):
        return self.category.title_ru

    def get_category_title_uz(self):
        return self.category.title_uz

    class Meta:
        verbose_name = 'Блюд'
        verbose_name_plural = 'Блюдо'
