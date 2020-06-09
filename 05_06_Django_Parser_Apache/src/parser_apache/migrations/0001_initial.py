# Generated by Django 3.0.6 on 2020-06-01 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Row_line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Строка лога')),
            ],
        ),
        migrations.CreateModel(
            name='Time_from_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateTimeField(verbose_name='Дата и время записи')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parser_apache.Row_line', verbose_name='Соответствующая дата')),
            ],
        ),
        migrations.CreateModel(
            name='Brousers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Браузеры')),
                ('brousers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parser_apache.Row_line', verbose_name='Браузеры')),
            ],
        ),
    ]