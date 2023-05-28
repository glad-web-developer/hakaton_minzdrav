from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.admin import RecomendationAssignmentInline
from api.models import Mkb10


@admin.register(Mkb10)
class Mkb10Admin(ImportExportModelAdmin):
    icon_name = 'book'
    inlines = [
        RecomendationAssignmentInline
    ]
    list_display = [
        'id',
        'name',
        'code',
    ]

    search_fields = [
        'id',
        'name',
        'code',
    ]
    list_display_links = [
        'id',
        'name',
        'code',
    ]

    save_as = True
    save_on_top = True
