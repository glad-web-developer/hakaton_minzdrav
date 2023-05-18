from django.db import models


class MedOrganization(models.Model):
    class Meta:
        verbose_name = 'Мед. организация'
        verbose_name_plural = 'Мед. организации'
        db_table = 'med_organization'

    name = models.CharField('Название', max_length=255, unique=True)