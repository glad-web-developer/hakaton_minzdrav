from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import Patient


@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
    icon_name = 'recent_actors'
    list_display = [
        'id',
        'fio',
        'sex',
        'date_birth',
    ]

    search_fields = [
        'id',
        'fio',
        'sex',
        'date_birth',
    ]
    list_display_links = [
        'id',
        'fio',
        'sex',
        'date_birth',
    ]
    list_filter = [
        'sex',
    ]

    save_as = True
    save_on_top = True
