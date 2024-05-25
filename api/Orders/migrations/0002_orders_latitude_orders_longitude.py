# Generated by Django 5.0.1 on 2024-05-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='latitude',
            field=models.CharField(blank=True, default=0, null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='orders',
            name='longitude',
            field=models.CharField(blank=True, default=0, null=True, verbose_name='Долгота'),
        ),
    ]