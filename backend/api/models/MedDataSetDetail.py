from django.contrib.auth.models import User
from django.db import models

from api.const import SOURCE_ENUM, IMPORT_DATA_SET_DETAIL_STATUS_ENUM
from api.models import MedDataSet


class MedDataSetDetail(models.Model):
    class Meta:
        verbose_name = 'Набор мед. назначений - детализация'
        verbose_name_plural = 'Наборы мед. назначений - детализация'
        db_table = 'med_data_set_detail'

    med_data_set = models.ForeignKey(MedDataSet, verbose_name='Набор данных', on_delete=models.CASCADE,)
    import_status = models.IntegerField('Статус импорта', choices=IMPORT_DATA_SET_DETAIL_STATUS_ENUM.choices)




    def __str__(self):
        return f'Набор №{self.id} от {self.date_create}'

