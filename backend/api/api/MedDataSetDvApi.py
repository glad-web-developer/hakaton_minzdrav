import math

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import MedDataSet
from api.serializers import CheckUserSerializerOut, MedDataSetLvSerializer, MedDataSetDvSerializer


class MedDataSetDvApi(APIView):

    def get(self, request, id):
        try:
            med_data_set = MedDataSet.objects.get(id=id)
        except MedDataSet.DoesNotExist:
            return Response({'message': 'Не найден набор данных по указанному id'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = MedDataSetDvSerializer(med_data_set, many=False)

        return Response({
            'data':serializer.data,
        })