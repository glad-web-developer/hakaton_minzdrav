import math

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import MedDataSet
from api.serializers import CheckUserSerializerOut, MedDataSetLvSerializer


class MedDataSetLvApi(APIView):

    def get(self, request):
        med_data_set = MedDataSet.objects.all()

        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 25))

        name = request.GET.get('name')
        # от
        date_create_from = request.GET.get('date_create_from')
        # до
        date_create_before = request.GET.get('date_create_before')
        source = request.GET.get('source')
        import_status = request.GET.get('import_status')

        if name:
            med_data_set = med_data_set.filter(name__icontains=name)
        if date_create_from:
            med_data_set = med_data_set.filter(date_create__gte=date_create_from)
        if date_create_before:
            med_data_set = med_data_set.filter(date_create__lte=date_create_before)
        if source:
            med_data_set = med_data_set.filter(source=source)
        if import_status:
            med_data_set = med_data_set.filter(import_status=import_status)

        count_row = med_data_set.count()
        page_count = math.ceil(count_row / limit)

        med_data_set = med_data_set[page*limit: (limit*page)+limit]

        serializer = MedDataSetLvSerializer(med_data_set, many=True)

        return Response({
            'data':serializer.data,
            'count_row':count_row,
            'page_count':page_count
        })