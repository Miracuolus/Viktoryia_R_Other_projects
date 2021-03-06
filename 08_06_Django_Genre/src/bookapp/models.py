from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название жанра',
        max_length= 100
    )
    description = models.TextField(
        verbose_name='Описание жанра',
        null=True, # БД позволяет хранить поле пустым
        blank=True, # сигнал Djange, что поле мб пустым
        help_text='Поле может быть пустым'
    )

    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length= 200
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        verbose_name='Жанр книги',
    )
    description = models.TextField(
        verbose_name='Описание книги',
        null=True, # БД позволяет хранить поле пустым
        blank=True, # сигнал Djange, что поле мб пустым
        help_text='Поле может быть пустым'
    )
    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )
    updated = models.DateTimeField(
        verbose_name='Изменено',
        auto_now=True, # автом ставить тек время
        auto_now_add=False # автом ставить время добавления
    )
    def __str__(self):
        return f'{self.name}: жанр - {self.genre}'
