from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.admin.MedDatasetDetailInline import MedDataSetDetailInline
from api.models import MedDataSet


@admin.register(MedDataSet)
class MedDataSetAdmin(ImportExportModelAdmin):
    icon_name = 'local_library'
    inlines = [MedDataSetDetailInline,]
    list_display = [
        'id',
        'name',
        'date_create',
        'source',
        'import_status',
        'count_correct',
        'count_dont_complete',
        'count_excess',
        'count_dont_correct',
    ]

    search_fields = [
        'id',
        'name',
        'date_create',
        'source',
        'import_status',
        'count_correct',
        'count_dont_complete',
        'count_excess',
        'count_dont_correct',
    ]
    list_display_links = [
        'id',
        'name',
        'date_create',
        'source',
        'import_status',
        'count_correct',
        'count_dont_complete',
        'count_excess',
        'count_dont_correct',
    ]

    list_filter = [
        'name',
        'source',
        'import_status',
        'is_excel',
    ]

    save_as = True
    save_on_top = True
