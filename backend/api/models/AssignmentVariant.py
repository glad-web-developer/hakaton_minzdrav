from django.db import models

from api.const import SOURCE_ENUM
from api.models import Assignment


class AssignmentVariant(models.Model):
    class Meta:
        verbose_name = 'Назначение - вариация названия'
        verbose_name_plural = 'Назначение - вариации названия'
        db_table = 'assignment_variant'

    assignment = models.ForeignKey(Assignment, max_length=255, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255,)