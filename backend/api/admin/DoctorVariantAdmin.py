from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import DoctorVariant


@admin.register(DoctorVariant)
class DoctorVariantAdmin(ImportExportModelAdmin):
    icon_name = 'supervisor_account'
    list_display = [
        'id',
        'doctor',
        'source',
        'source_fio',
        'source_id',
        'source_specialization',
    ]

    search_fields = [
        'id',
        'doctor',
        'source',
        'source_fio',
        'source_id',
        'source_specialization',
    ]
    list_display_links = [
        'id',
        'doctor',
        'source',
        'source_fio',
        'source_id',
        'source_specialization',
    ]
    list_filter = [
        'source',
    ]
    save_as = True
    save_on_top = True
