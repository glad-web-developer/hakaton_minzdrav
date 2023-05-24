from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import MedUser


@admin.register(MedUser)
class MedUserAdmin(ImportExportModelAdmin):
    icon_name = 'people'
    list_display = [
        'id',
        'user',
        'fio',
        'med_organiizaciya',
        'role',
    ]

    search_fields = [
        'id',
        'user.useranme',
        'user',
        'med_organiizaciya.name',
    ]
    list_display_links = [
        'id',
        'user',
        'fio',
        'med_organiizaciya',
        'role',
    ]

    list_filter = ['role',]

    save_as = True
    save_on_top = True
