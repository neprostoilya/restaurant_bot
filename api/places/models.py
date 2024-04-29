from django.db import models
from django.utils.safestring import mark_safe


class Places(models.Model):
    """
    Model Places
    """
    title_ru = models.CharField(
        verbose_name='Название RU'
    )
    title_uz = models.CharField(
        verbose_name='Название UZ'
    )
    is_view = models.BooleanField(
        verbose_name='Показывать',
        default=True
    )
        
    def __str__(self) -> str:
        return self.title_ru
    
    def __repr__(self) -> str:
        return super().__repr__()

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'