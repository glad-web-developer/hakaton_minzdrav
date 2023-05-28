from django.contrib import admin

from .models import Dashboard, Widget, WidgetCoordinates


@admin.register(WidgetCoordinates)
class WidgetCoordinatesAdmin(admin.ModelAdmin):
    pass


@admin.register(Widget)
class WidgetAdmin(admin.ModelAdmin):
    pass


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    pass
