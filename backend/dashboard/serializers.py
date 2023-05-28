from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from dashboard.models import Widget, Dashboard, WidgetCoordinates


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = '__all__'


class WidgetCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidgetCoordinates
        fields = '__all__'


class DashboardSerializer(serializers.ModelSerializer):
    widgets = serializers.SerializerMethodField('get_dashboard_widgets')

    class Meta:
        model = Dashboard
        fields = '__all__'

    def get_dashboard_widgets(self, instance):
        widgets_coords = WidgetCoordinates.objects.filter(dashboard=instance)

        response = []
        for coords in widgets_coords:
            response.append({
                **WidgetSerializer(coords.widget).data,
                **WidgetCoordinatesSerializer(coords).data
            })

        return response

    def create(self, validated_data):
        print(validated_data)
        title = validated_data.pop('title')
        widgets_data = validated_data.pop('widgets')

        dashboard = Dashboard(title=title)
        dashboard.save()

        for wd in widgets_data:
            widget = Widget.objects.filter(id=wd['id']).first()
            WidgetCoordinates.objects.get_or_create(
                dashboard=dashboard,
                widget=widget,
                x=wd['x'],
                y=wd['y']
            )

        return dashboard

    def to_internal_value(self, data):
        title = data.get('title', None)
        if title is None or not isinstance(title, str):
            raise ValidationError(detail='Поле title - обязательно и должно быть типа str')

        return data
