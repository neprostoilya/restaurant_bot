from django.db import models
from categories.models import Categories

from django.utils.safestring import mark_safe


class Dishes(models.Model):
    """
    Model Dishes
    """
    image = models.ImageField(
        upload_to='dishes/', 
        verbose_name='Изображение'
    )
    title_ru = models.CharField(
        max_length=155,
        verbose_name='Название блюда RU'
    )
    title_uz = models.CharField(
        max_length=155,
        verbose_name='Название блюда UZ'
    )
    description_ru = models.TextField(
        verbose_name='Описание RU'
    )
    description_uz = models.TextField(
        verbose_name='Описание UZ'
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
         return self.title_ru

    def __repr__(self) -> str:
         return (f'Dishes: image={self.image}, title_ru={self.title_ru}, title_uz={self.title_uz}, description_ru={self.description_ru},'
                 f' description_uz={self.description_uz}, category={self.category}, price={self.price}')
    
    def descriptiontrim_ru(self):
        return u"%s" % (self.description_ru[:35],) + '...'
    
    descriptiontrim_ru.allow_tags = True
    descriptiontrim_ru.short_description = 'Описание'

    def descriptiontrim_uz(self):
        return u"%s" % (self.description_ru[:35],) + '...'
    
    descriptiontrim_ru.allow_tags = True
    descriptiontrim_ru.short_description = 'Описание'

    def img_preview(self): 
            return mark_safe(f'<img src="{self.image.url}" width="100px" height="100px"/>')
    
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    def get_category_title(self):
        return self.category.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'
