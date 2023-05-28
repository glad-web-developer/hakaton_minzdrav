from rest_framework import serializers

from api.models import MedDataSet, MedDataSetDetail
from api.serializers.Mkb10Serializer import Mkb10Serializer


class MedDataSetDetailLvSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedDataSetDetail
        fields = '__all__'

    mkb10 = Mkb10Serializer(many=False)