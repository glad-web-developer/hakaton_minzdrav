from rest_framework import serializers

from api.models import MedDataSet
from api.serializers import MedDataSetDetailLvSerializer


class MedDataSetDvSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedDataSet
        fields = '__all__'

    items = MedDataSetDetailLvSerializer(many=True, read_only=True, source='meddatasetdetail_set')


