from django.db import models

from api.const import SOURCE_ENUM


class Mkb10(models.Model):
    class Meta:
        verbose_name = 'МКБ10'
        verbose_name_plural = 'МКБ10'
        db_table = 'mkb10'

    name = models.CharField('Название', max_length=255, unique=True)
    code = models.CharField('Код', max_length=255, unique=True)

    def __str__(self):
        return f'{self.code} {self.name}'