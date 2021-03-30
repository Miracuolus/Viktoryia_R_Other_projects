# Generated by Django 3.0.7 on 2020-06-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, help_text='Поле может быть пустым', null=True, verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, help_text='Поле может быть пустым', null=True, verbose_name='Описание жанра'),
        ),
    ]