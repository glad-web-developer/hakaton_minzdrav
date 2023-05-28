from rest_framework import serializers

from api.models import MedDataSet, MedDataSetDetail, Mkb10


class Mkb10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mkb10
        fields = '__all__'
