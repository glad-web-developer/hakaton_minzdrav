from django.db import models

from api.const import SOURCE_ENUM


class DoctorVariant(models.Model):
    class Meta:
        verbose_name = 'Доктор/врач - вариации в разных системах'
        verbose_name_plural = 'Доктора/врачи- вариации в разных системах'
        db_table = 'doctor_variant'


    source = models.IntegerField('Источник данных', choices=SOURCE_ENUM.choices)
    source_fio = models.CharField('ФИО во внешней системе', max_length=255, )
    # id может быть UUID строка и int
    source_id = models.CharField('id во внешней системе', max_length=255)
    source_specialization = models.CharField('Специализация во внешней системе', max_length=255)

    def __str__(self):
        return self.fio