# Generated by Django 5.0.1 on 2024-01-23 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категорию Блюда', 'verbose_name_plural': 'Категории Блюд'},
        ),
        migrations.RemoveField(
            model_name='categories',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='title_uz',
        ),
        migrations.AddField(
            model_name='categories',
            name='title',
            field=models.CharField(default=68, max_length=100, verbose_name='Название категории'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Subategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название подкатегории')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Categories.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегорию Блюда',
                'verbose_name_plural': 'Подкатегории Блюд',
            },
        ),
    ]