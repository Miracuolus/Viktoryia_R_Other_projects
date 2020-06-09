# Generated by Django 3.0.6 on 2020-06-01 17:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 6, 1, 17, 40, 58, 432000, tzinfo=utc), verbose_name='Создано'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменено'),
        ),
    ]
