from django.db import models

from api.const import SOURCE_ENUM
from api.models import Assignment


class AssignmentVariant(models.Model):
    class Meta:
        verbose_name = 'Назначение - вариация названия'
        verbose_name_plural = 'Назначение - вариации названия'
        db_table = 'assignment_variant'

    assignment = models.ForeignKey(Assignment, max_length=255, on_delete=models.CASCADE, verbose_name='Назначение(родительская запись в БД)', null=True, blank=True)
    name = models.CharField('Название', max_length=255,)
    source = models.IntegerField('Источник данных', choices=SOURCE_ENUM.choices)