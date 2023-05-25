from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import AssignmentVariant


@admin.register(AssignmentVariant)
class AssignmentVariantAdmin(ImportExportModelAdmin):
    icon_name = 'assignment'
    list_display = [
        'id',
        'name',
        'assignment',
    ]

    search_fields = [
        'id',
        'name',
        'assignment',
    ]
    list_display_links = [
        'id',
        'name',
        'assignment',
    ]
    list_filter = [
        'assignment',
    ]
    save_as = True
    save_on_top = True
