from django.db import models

from api.const import SOURCE_ENUM, SEX_ENUM
from api.models import Patient


class PatientVariant(models.Model):
    class Meta:
        verbose_name = 'Пациент - вариации в разных системах'
        verbose_name_plural = 'Пациенты- вариации в разных системах'
        db_table = 'patient_variant'


    patient = models.ForeignKey(Patient, verbose_name='Пациент(родительская запись в БД)', on_delete=models.CASCADE)
    source = models.IntegerField('Источник данных', choices=SOURCE_ENUM.choices)
    source_fio = models.CharField('ФИО во внешней системе', max_length=255, )
    # id может быть UUID строка и int
    source_id = models.CharField('id во внешней системе', max_length=255)
    source_sex = models.IntegerField('Пол', choices=SEX_ENUM.choices, null=True, blank=True)
    source_date_birth = models.DateField('Дата рождения', null=True, blank=True)
    source_snils = models.CharField('СНИЛС', max_length=255, null=True, blank=True)
    source_passport = models.CharField('Серия и номер паспорта', max_length=255, null=True, blank=True)
    source_polis = models.CharField('Номер полиса', max_length=255, null=True, blank=True)
    source_phone = models.CharField('Телефон', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.source_fio