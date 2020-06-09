# Generated by Django 3.0.6 on 2020-06-03 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parser_apache', '0026_auto_20200603_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='parser',
            name='brou',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parser_apache.Brouser', verbose_name='Браузер лога'),
        ),
        migrations.AddField(
            model_name='parser',
            name='bо',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parser_apache.Bot', verbose_name='Бот лога'),
        ),
    ]
