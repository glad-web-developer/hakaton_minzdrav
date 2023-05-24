from django.db import models

from api.const import IMPORT_DATA_SET_DETAIL_STATUS_ENUM, SEX_ENUM
from api.models import MedDataSet, Mkb10


class MedDataSetDetail(models.Model):
    class Meta:
        verbose_name = 'Набор мед. назначений - детализация'
        verbose_name_plural = 'Наборы мед. назначений - детализация'
        db_table = 'med_data_set_detail'

    med_data_set = models.ForeignKey(MedDataSet, verbose_name='Набор данных', on_delete=models.CASCADE,)
    import_status = models.IntegerField('Статус импорта', choices=IMPORT_DATA_SET_DETAIL_STATUS_ENUM.choices)
    # id может быть UUID строка и int
    source_appointment_id = models.CharField('id приёма во внешней системе', max_length=255)
    patient_source_fio = models.CharField('ФИО пациента во внешней системе', null=True, blank=True, max_length=255)
    patient_source_id = models.CharField('id пациента во внешней системе', max_length=255)
    mkb10 = models.ForeignKey(Mkb10, verbose_name='Диагноз МКБ 10', on_delete=models.PROTECT)

    patient_sex = models.IntegerField('Пол пациента', choices=SEX_ENUM.choices, null=True, blank=True)
    patient_date_birth = models.DateField('Дата рождения пациента', null=True, blank=True)

