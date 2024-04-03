from django.db import models
from django.utils.safestring import mark_safe


class Events(models.Model):
    """
    Model Events while month
    """
    image = models.ImageField(
        verbose_name='Фотокарточка'
    )
    description_ru = models.TextField(
        verbose_name='Описание RU'
    )
    description_uz = models.TextField(
        verbose_name='Описание UZ'
    )
    
    def descriptiontrim(self):
        return u"%s" % (self.description_ru[:35],) + '...'
    
    descriptiontrim.allow_tags = True
    descriptiontrim.short_description = 'Описание'
    
    def __str__(self) -> str:
        return self.image.url
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def img_preview(self): 
        return mark_safe(f'<img src="{self.image.url}" width="100px" height="75px"/>')
    
    img_preview.allow_tags = True
    img_preview.short_description = 'Миниатюра'

    class Meta:
        verbose_name = 'Эвент'
        verbose_name_plural = 'Эвенты'