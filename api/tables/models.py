from django.db import models


class Tables(models.Model):
    """
    Model Tables
    """
    number = models.IntegerField(
        verbose_name='Номер стола'
    )

    status = models.CharField(
        verbose_name='Статус',
        default='Свободен'
    )
    
    
    def __str__(self) -> str:
        return str(self.number)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'