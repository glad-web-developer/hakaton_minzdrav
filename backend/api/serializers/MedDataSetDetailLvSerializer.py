from rest_framework import serializers

from api.models import MedDataSet, MedDataSetDetail


class MedDataSetDetailLvSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedDataSetDetail
        fields = '__all__'
