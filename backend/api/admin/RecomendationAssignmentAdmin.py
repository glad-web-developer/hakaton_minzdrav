from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import AssignmentVariant, AllAssignment, RecomendationAssignment


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
        'assignment__name',
        'mkb10__name',
    ]
    list_display_links = [
        'id',
        'assignment',
        'mkb10',
    ]

    save_as = True
    save_on_top = True
