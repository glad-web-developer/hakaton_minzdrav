from django.db import models

from api.const import SOURCE_ENUM


class Doctor(models.Model):
    class Meta:
        verbose_name = 'Доктор/врач'
        verbose_name_plural = 'Доктора/врачи'
        db_table = 'doctor'

    fio = models.CharField('ФИО', max_length=255, )
    # id может быть UUID строка и int
    specialization = models.CharField('Специализация', max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.fio} - {self.specialization if self.specialization else ""}'