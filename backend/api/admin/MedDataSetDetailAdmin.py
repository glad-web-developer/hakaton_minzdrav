from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import MedDataSetDetail


@admin.register(MedDataSetDetail)
class MedDataSetDetailAdmin(ImportExportModelAdmin):
    icon_name = 'list'
    list_display = [
        'id',
        'med_data_set',
        'import_status',
        'patient_source_fio',
        'patient_source_id',
        'mkb10',
        'doctor_source_id',
        'doctor_source_fio',
        'assignment_string',
    ]

    search_fields = [
        'id',
        'med_data_set',
        'import_status',
        'patient_source_fio',
        'patient_source_id',
        'mkb10',
        'doctor_source_id',
        'doctor_source_fio',
        'assignment_string',
    ]
    list_display_links = [
        'id',
        'med_data_set',
        'import_status',
        'patient_source_fio',
        'patient_source_id',
        'mkb10',
        'doctor_source_id',
        'doctor_source_fio',
        'assignment_string',
    ]

    save_as = True
    save_on_top = True
