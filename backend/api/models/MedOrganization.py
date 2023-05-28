from django.db import models

from api.const import SOURCE_ENUM


class MedOrganization(models.Model):
    class Meta:
        verbose_name = 'Мед. организация'
        verbose_name_plural = 'Мед. организации'
        db_table = 'med_organization'

    name = models.CharField('Название', max_length=255, unique=True)
    source = models.IntegerField('Источник данных', choices=SOURCE_ENUM.choices)
    # id может быть UUID строка и int
    source_id = models.CharField('id во внешней системе', max_length=255)


    def __str__(self):
        return self.name