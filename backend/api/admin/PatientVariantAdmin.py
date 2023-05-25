from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import PatientVariant


@admin.register(PatientVariant)
class PatientVariantAdmin(ImportExportModelAdmin):
    icon_name = 'supervisor_account'
    list_display = [
        'id',
        'patient',
        'source',
        'source_fio',
        'source_id',
        'source_sex',
        'source_date_birth',
    ]

    search_fields = [
        'id',
        'patient',
        'source',
        'source_fio',
        'source_id',
        'source_sex',
        'source_date_birth',
    ]
    list_display_links = [
        'id',
        'patient',
        'source',
        'source_fio',
        'source_id',
        'source_sex',
        'source_date_birth',
    ]

    list_filter = ['source_sex',]

    save_as = True
    save_on_top = True
