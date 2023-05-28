from django.contrib import admin

from api.models import MedDataSetDetail


class MedDataSetDetailInline(admin.TabularInline):
    model = MedDataSetDetail
    extra = 0
    autocomplete_fields = ['mkb10']