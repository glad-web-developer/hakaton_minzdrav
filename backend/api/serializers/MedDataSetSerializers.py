from rest_framework import serializers

from api.models import MedDataSet


class MedDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedDataSet
        fields = '__all__'
