from django.db import models

from api.const import SEX_ENUM


class Patient(models.Model):
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        db_table = 'patient'

    fio = models.CharField('ФИО', max_length=255,)
    sex = models.IntegerField('Пол', choices=SEX_ENUM.choices, null=True, blank=True)
    date_birth = models.DateField('Дата рождения', null=True, blank=True)

    def __str__(self):
        return self.fio