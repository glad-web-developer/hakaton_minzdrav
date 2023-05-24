from django.db import models

from api.const import IMPORT_DATA_SET_DETAIL_STATUS_ENUM, SEX_ENUM
from api.models import MedDataSet, Mkb10


class MedDataSetDetail(models.Model):
    class Meta:
        verbose_name = 'Набор мед. назначений - детализация'
        verbose_name_plural = 'Наборы мед. назначений - детализация'
        db_table = 'med_data_set_detail'

    med_data_set = models.ForeignKey(MedDataSet, verbose_name='Набор данных', on_delete=models.CASCADE,)
    row_num = models.IntegerField('Номер строки')
    import_status = models.IntegerField('Статус импорта', choices=IMPORT_DATA_SET_DETAIL_STATUS_ENUM.choices)
    patient_sex = models.IntegerField('Пол пациента', choices=SEX_ENUM.choices, null=True, blank=True)
    patient_date_birth = models.DateField('Дата рождения пациента', null=True, blank=True)
    # id может быть UUID строка и int
    source_appointment_id = models.CharField('ID приёма во внешней системе', max_length=255)
    patient_source_fio = models.CharField('ФИО пациента во внешней системе', null=True, blank=True, max_length=255)
    patient_source_id = models.CharField('ID пациента во внешней системе', max_length=255)
    mkb10 = models.ForeignKey(Mkb10, verbose_name='Диагноз МКБ 10', on_delete=models.PROTECT)
    date_service = models.DateField(verbose_name='Дата услуги',)
    doctor_source_id = models.CharField('ID доктора во внешней системе', max_length=255)
    doctor_source_fio = models.CharField('ФИО доктора во внешней системе', max_length=255, null=True, blank=True)
    doctor_source_specialization = models.CharField('Специализация доктора во внешней системе', max_length=255, null=True, blank=True)
    assignment_string = models.TextField('Строка с назначениями')

    def __str__(self):
        # так как у экселя первая строка эта шапка, то для удобства поиска нужной строки мы делаем нумерацию как в экселе
        if self.med_data_set.is_excel:
            return f'строка № {self.row_num + 1} '

        # для API номер строки как есть
        return f'строка № {self.row_num} '
