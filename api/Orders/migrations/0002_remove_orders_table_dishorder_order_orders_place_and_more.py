# Generated by Django 5.0.1 on 2024-05-09 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('places', '0002_places_is_view'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='dishorder',
            name='order',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='orders.orders', verbose_name='Заказ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.places', verbose_name='Место'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='people_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Кол-во людей'),
        ),
    ]