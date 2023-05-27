
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.const import IMPORT_EXCEL_TEMPLATE_ENUM
from api.serializers import LoginSerializer

# формирует url дял фронта по которому можно скачать шаблон импорта через эксель
class UrlImportTemplate(APIView):
    def get(self, request, template_name=None):
        if template_name:
            template_url = IMPORT_EXCEL_TEMPLATE_ENUM.get_path(template_name)
            return Response(template_url) if template_url else Response('Передан неизвестный тип ')
        else:
            return Response(f'Не указан параметр /<template_name>/. Возможные значения: {IMPORT_EXCEL_TEMPLATE_ENUM.values}')

