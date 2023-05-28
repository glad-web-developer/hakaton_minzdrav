from django.contrib import admin

from api.models import RecomendationAssignment


class RecomendationAssignmentInline(admin.TabularInline):
    model = RecomendationAssignment
    extra = 0
    autocomplete_fields = ['mkb10', 'assignment']