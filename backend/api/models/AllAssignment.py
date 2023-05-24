from django.db import models

from api.const import ASSIGNMENT_STATUS_ENUM
from api.models import MedDataSetDetail, Assignment


class AllAssignment(models.Model):
    class Meta:
        verbose_name = 'Все назначения'
        verbose_name_plural = 'Все назначения'
        db_table = 'all_assignment'

    # todo тут не хвататает полей для определения уникальности. Подумать на свежую голову
    #  is_archive добавить + продумать как перерасчет делать если были записи до него. Как вариант выборка по id source + last наборы. Или цикл по тем что в архив и поиск по последнему набору
    #    тут вероятно не назначения надо а диагнозы и правильности назначений !!!ВАЖНО

    med_data_set = models.ForeignKey(MedDataSetDetail, verbose_name='Набор данных - детализация',
                                     on_delete=models.CASCADE, )
    source_assignment = models.CharField('Назначение во внешней системе', max_length=255)
    assignment = models.ForeignKey(Assignment, null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name='Сопоставленное назначение')
    assignment_status = models.IntegerField('Статус правильности назначения', choices=ASSIGNMENT_STATUS_ENUM.choices)

    def __str__(self):
        return f'Назначение №{self.id}'
