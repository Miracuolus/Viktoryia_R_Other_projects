# Generated by Django 3.0.6 on 2020-06-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_apache', '0017_parser_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parser',
            name='system',
            field=models.TextField(blank=True, null=True, verbose_name='Информация о системе'),
        ),
    ]
