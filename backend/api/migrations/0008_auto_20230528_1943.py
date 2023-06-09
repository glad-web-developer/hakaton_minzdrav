# Generated by Django 3.2.2 on 2023-05-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20230527_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meddataset',
            name='excel_in',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='excel на входе'),
        ),
        migrations.AlterField(
            model_name='meddataset',
            name='excel_out',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='excel с ошибками на выходе'),
        ),
        migrations.AlterField(
            model_name='meddataset',
            name='import_status',
            field=models.IntegerField(choices=[(1, 'Успешный импорт'), (2, 'Не все записи импортированы'), (3, 'Ошибка чтения файла'), (4, 'Ошибка структуры файла или запроса'), (5, 'Ошибка прав доступа')], verbose_name='Статус импорта'),
        ),
        migrations.AlterField(
            model_name='meddataset',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='Набор отправлен в архив'),
        ),
    ]
