from django.contrib import admin

from api.models import PatientVariant


class PatientVariantInline(admin.TabularInline):
    model = PatientVariant
    extra = 0
    autocomplete_fields = ['patient', ]