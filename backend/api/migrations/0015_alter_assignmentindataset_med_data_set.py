# Generated by Django 3.2.2 on 2023-05-29 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20230529_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentindataset',
            name='med_data_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.meddatasetdetail', verbose_name='Набор данных - детализация'),
        ),
    ]