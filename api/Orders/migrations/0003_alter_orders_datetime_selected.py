# Generated by Django 5.0.1 on 2024-03-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orders_people_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='datetime_selected',
            field=models.TimeField(verbose_name='Указанное время'),
        ),
    ]