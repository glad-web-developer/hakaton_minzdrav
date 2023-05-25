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
    snils = models.DateField('СНИЛС', null=True, blank=True)
    passport = models.DateField('Серия и номер паспорта', null=True, blank=True)
    polis = models.DateField('Номер полиса', null=True, blank=True)
    phone = models.CharField('Телефон', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.fio