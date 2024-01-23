# Generated by Django 5.0.1 on 2024-01-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0002_alter_dishes_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishes',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюдо'},
        ),
        migrations.AlterField(
            model_name='dishes',
            name='price',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Цена'),
        ),
    ]