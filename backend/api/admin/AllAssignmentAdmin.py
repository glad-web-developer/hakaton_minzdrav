from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import AssignmentVariant, AllAssignment


@admin.register(AllAssignment)
class AllAssignmentAdmin(ImportExportModelAdmin):
    icon_name = 'assignment'
    list_display = [
        'id',
        'med_data_set',
        'source_assignment',
        'assignment',
        'assignment_status',
    ]

    search_fields = [
        'id',
        'med_data_set',
        'source_assignment',
        'assignment',
        'assignment_status',
    ]
    list_display_links = [
        'id',
        'med_data_set',
        'source_assignment',
        'assignment',
        'assignment_status',
    ]
    list_filter = [
        'med_data_set',
        'source_assignment',
        'assignment',
        'assignment_status',
    ]
    save_as = True
    save_on_top = True
