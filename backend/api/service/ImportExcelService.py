from django.contrib.auth.models import User

from api.const import IMPORT_EXCEL_TEMPLATE_ENUM, SOURCE_ENUM, IMPORT_DATA_SET_STATUS_ENUM
from api.models import MedDataSet, Mkb10
from api.service import ImportService
import pandas as pd


class ImportExcelService(ImportService):
    HEADER_MIS_MOSCOW = [
        {
            'label': 'ID пациента*',
            'name': 'patient_id',
            'required': True
        },
        {
            'label': 'ФИО пациента',
            'name': 'patient_fio',
            'required':False
        },
        {
            'label': 'Пол пациента',
            'name': 'patient_sex',
            'required': False
        },
        {
            'label': 'Дата рождения пациента',
            'name': 'patient_date_birth',
            'required': False
        },
        {
            'label': 'Номер полиса пациента',
            'name': 'patient_polis',
            'required': False
        },
        {
            'label': 'СНИЛС пациента',
            'name': 'patient_snils',
            'required': False
        },
        {
            'label': 'Телефон пациента',
            'name': 'patient_phone',
            'required': False
        },
        {
            'label': 'Номер паспорта пациента',
            'name': 'patient_passport',
            'required': False
        },
        {
            'label': 'ID приема*',
            'name': 'med_data_set_detail_id',
            'required': True
        },
        {
            'label': 'Дата оказания услуги*',
            'name': 'date_service',
            'required': True
        },
        {
            'label': 'ID врача*',
            'name': 'doctor_source_id',
            'required': True
        },
        {
            'label': 'ФИО врача',
            'name': 'doctor_source_fio',
            'required': False
        },
        {
            'label': 'Должность',
            'name': 'doctor_source_specialization',
            'required': False
        },
        {
            'label': 'Код МКБ-10*',
            'name': 'mkb10__code',
            'required': True
        },
        {
            'label': 'Назначения*',
            'name': 'assignment_string',
            'required': True
        },
    ]

    def get_header(self, excel_template: IMPORT_EXCEL_TEMPLATE_ENUM):
        """
        вернёт список названий полей который ожидаються в Excel файле
        """
        if excel_template == IMPORT_EXCEL_TEMPLATE_ENUM.MIS_MOSCOW:
            return self.HEADER_MIS_MOSCOW

    def get_required_header(self, excel_template: IMPORT_EXCEL_TEMPLATE_ENUM):
        header = self.get_header(excel_template)
        item_header_list = list(filter(lambda x: (x['required']), header))
        return list(map(lambda x:x['label'], item_header_list))



    def check_data(self, excel_ds, excel_template: IMPORT_EXCEL_TEMPLATE_ENUM):
        """
        Проверяет данные на соотвествие
        """
        required_filds_list = self.get_required_header(excel_template)
        check_data_error_list = []
        for index_row, row in enumerate(excel_ds, start=1):
            error_column_list = []

            for column_label, row_val in row.items():
                if column_label in required_filds_list:
                    if pd.isnull(row_val) or not row_val:
                        error_column_list.append(column_label)

                if column_label =='Код МКБ-10*':
                    try:
                        Mkb10.objects.get(code=row_val)
                    except Mkb10.DoesNotExist:
                        check_data_error_list.append({
                            'row': index_row,
                            'error': f'Неизвестный код МКБ10: "{row_val}"'
                        })

            if error_column_list:
                check_data_error_list.append({
                    'row':index_row,
                    'error': f'Нет значения в поле/полях: {",".join(error_column_list)}'
                })
        return check_data_error_list



    def check_structure(self, excel_ds, excel_template: IMPORT_EXCEL_TEMPLATE_ENUM):
        """
        Проверка, структура соответствует шаблону + вытащить данные в DataSet
        """

        # получаем шапку excel и проверяем её с настойками полей импорта
        excel_ds_header = list(excel_ds.columns)

        excel_template_header = self.get_header(excel_template=excel_template)

        # проверка на достаточность полей
        columns_dont_exist = []
        for column_header in excel_template_header:
            if not (column_header['label'] in excel_ds_header) and column_header['required']:
                columns_dont_exist.append(column_header['label'])

        return columns_dont_exist



    def revert_import(self):
        """
        отмена импорта
        """

    def save_log(self):
        pass

    def check_assignment(self, excel_ds, ):
        """
        проверка назначений
        """
        pass



    def import_excel(self, excel_file, user: User, source:SOURCE_ENUM,
                     excel_template: IMPORT_EXCEL_TEMPLATE_ENUM = IMPORT_EXCEL_TEMPLATE_ENUM.MIS_MOSCOW, data_set_name = ''):
        """
        запуск импорта excel файла
        """
        med_data_set = MedDataSet(
            user=user,
            name=data_set_name,
            is_excel=True,
            source=source,
            excel_in=excel_file
        )

        # проверка на формат файла
        if excel_file.content_type != 'application/vnd.ms-excel' and excel_file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            med_data_set.import_status=IMPORT_DATA_SET_STATUS_ENUM.ERROR_FILE
            med_data_set.save()
            raise Exception(f'Ошибка чтения файла или файл не является Excel')

        # вытаскиваем данные
        excel_ds = pd.read_excel(excel_file, sheet_name=0)

        # проверяем структуру
        columns_dont_exist = self.check_structure(excel_ds, excel_template)

        if columns_dont_exist:
            med_data_set.import_status = IMPORT_DATA_SET_STATUS_ENUM.ERROR_STRUCTURE
            med_data_set.save()
            raise Exception(f'В Excel файле нехватает полей: {columns_dont_exist}')

        # меняем структуру представления данных
        excel_ds = excel_ds.to_dict('records')


        data_error_list = self.check_data(excel_ds=excel_ds, excel_template=excel_template)

        if data_error_list:
            med_data_set.import_status = IMPORT_DATA_SET_STATUS_ENUM.ERROR_REQUIRED
            med_data_set.count_rows = len(excel_ds)
            med_data_set.count_error = len(data_error_list)
            med_data_set.save()
            raise Exception(data_error_list)

        self.check_assignment(excel_ds=excel_ds)