# Generated by Django 3.0.6 on 2020-06-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_apache', '0019_auto_20200603_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='parser',
            name='byte',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Кол-во отправленных байтов клиенту'),
        ),
        migrations.AddField(
            model_name='parser',
            name='status',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Статус ответа сервера'),
        ),
    ]