from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.admin import DoctorVariantInline
from api.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(ImportExportModelAdmin):
    icon_name = 'recent_actors'
    inlines = [
        DoctorVariantInline,
    ]
    list_display = [
        'id',
        'fio',
        'specialization',
    ]

    search_fields = [
        'id',
        'fio',
        'specialization',
    ]
    list_display_links = [
        'id',
        'fio',
        'specialization',
    ]
    list_filter = [
        'specialization',
    ]
    save_as = True
    save_on_top = True
