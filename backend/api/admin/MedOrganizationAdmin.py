from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import MedOrganization


@admin.register(MedOrganization)
class MedOrganizationAdmin(ImportExportModelAdmin):
    icon_name = 'local_hospital'
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
