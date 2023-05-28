from django.contrib import admin

from api.models import DoctorVariant


class DoctorVariantInline(admin.TabularInline):
    model = DoctorVariant
    extra = 0
    autocomplete_fields = ['doctor', ]