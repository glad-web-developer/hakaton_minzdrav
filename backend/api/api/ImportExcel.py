from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.service import ImportExcelService


class ImportExcel(APIView):
    def post(self, request, template_name=None):
        excel_file = request.FILES['excel'] if 'excel' in request.FILES else None
        if excel_file:
            import_excel_service = ImportExcelService()

            import_excel_service.import_excel(excel_file)

            try:
                import_excel_service.import_excel(excel_file)
                return Response({'message':'Импорт прошёл успешно'})
            except Exception as e:
                return Response({'message':f'Ошибка при импорте файла: {e}'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message':'Ошибка запроса. В запросе по ключу "excel" ожидался файл'},
                            status=status.HTTP_400_BAD_REQUEST)
