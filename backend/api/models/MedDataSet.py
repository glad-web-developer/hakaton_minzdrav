from django.contrib.auth.models import User
from django.db import models

from api.const import SOURCE_ENUM, IMPORT_DATA_SET_STATUS_ENUM


class MedDataSet(models.Model):
    class Meta:
        verbose_name = 'Набор мед. назначений'
        verbose_name_plural = 'Наборы мед. назначений'
        db_table = 'med_data_set'

    user = models.ForeignKey(User, verbose_name='Пользователь кто импортировал', on_delete=models.PROTECT,)
    name = models.CharField('Название набора', null=True, blank=True, max_length=255)
    date_create = models.DateTimeField('Дата импорта', auto_now_add=True)
    is_excel = models.BooleanField('Импорт был через Эксель', default=False)
    is_archive = models.BooleanField('Набор отправлен в архив', default=False, help_text='не будет учитываться в наборе')
    source = models.IntegerField('Источник данных', choices=SOURCE_ENUM.choices)
    import_status = models.IntegerField('Статус импорта', choices=IMPORT_DATA_SET_STATUS_ENUM.choices)

    excel_in = models.FileField('excel на входе', null=True, blank=True, help_text='если импорт был не через API')
    excel_out = models.FileField('excel с ошибками на выходе', null=True, blank=True, help_text='если импорт был с ошибкой')

    count_rows = models.IntegerField('Количество строк данных', null=True, blank=True)
    count_error = models.IntegerField('Количество ошибочных строк', null=True, blank=True)

    count_correct = models.IntegerField('Количество правильных назначений', null=True, blank=True)
    count_dont_complete = models.IntegerField('Количество неполных назначений', null=True, blank=True)
    count_excess = models.IntegerField('Количество избыточных назначений', null=True, blank=True)
    count_dont_correct = models.IntegerField('Количество неверных назначений', null=True, blank=True)

    def __str__(self):
        return f'Набор №{self.id} от {self.date_create}'

