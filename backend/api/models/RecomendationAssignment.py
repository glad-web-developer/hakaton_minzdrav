from django.db import models

from api.const import SOURCE_ENUM
from api.models import Assignment, Mkb10


class RecomendationAssignment(models.Model):
    class Meta:
        verbose_name = 'Рекомендации по назначению'
        verbose_name_plural = 'Рекомендации по назначению'
        db_table = 'recomendation_assignment'

    assignment = models.ForeignKey(Assignment,verbose_name='Назначение', on_delete=models.CASCADE)
    mkb10 = models.ForeignKey(Mkb10, verbose_name='МКБ10', on_delete=models.CASCADE)