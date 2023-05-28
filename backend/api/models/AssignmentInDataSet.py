from django.db import models

from api.const import ASSIGNMENT_STATUS_ENUM
from api.models import MedDataSetDetail, Assignment


class AssignmentInDataSet(models.Model):
    class Meta:
        verbose_name = 'Назанчение в наборах данных'
        verbose_name_plural = 'Назанчения в наборах данных'
        db_table = 'assignment_in_data_set'

    # +
    med_data_set = models.ForeignKey(MedDataSetDetail, verbose_name='Набор данных - детализация', on_delete=models.CASCADE, null=True, blank=True)
    source_assignment = models.CharField('Назначение во внешней системе', max_length=255)
    assignment = models.ForeignKey(Assignment, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Сопоставленное назначение')
    assignment_status = models.IntegerField('Статус правильности назначения', choices=ASSIGNMENT_STATUS_ENUM.choices)

    def __str__(self):
        return self.source_assignment