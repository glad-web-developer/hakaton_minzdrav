from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.admin import RecomendationAssignmentInline
from api.models import Assignment


@admin.register(Assignment)
class AssignmentAdmin(ImportExportModelAdmin):
    icon_name = 'healing'
    inlines = [
        RecomendationAssignmentInline
    ]
    list_display = [
        'id',
        'name',
    ]

    search_fields = [
        'id',
        'name',
    ]
    list_display_links = [
        'id',
        'name',
    ]
    save_as = True
    save_on_top = True
