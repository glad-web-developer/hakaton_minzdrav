# Generated by Django 3.2.2 on 2023-05-27 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230525_2238'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientVariant',
        ),
    ]