from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import RecomendationAssignment


@admin.register(RecomendationAssignment)
class RecomendationAssignmentAdmin(ImportExportModelAdmin):
    icon_name = 'assignment'
    list_display = [
        'id',
        'assignment',
        'mkb10',
    ]

    search_fields = [
        'id',
        'assignment.name',
        'mkb10.name',
        'mkb10.code',
    ]
    list_display_links = [
        'id',
        'assignment',
        'mkb10',
    ]
    list_filter = [
        'assignment',
        'mkb10',
    ]
    save_as = True
    save_on_top = True
