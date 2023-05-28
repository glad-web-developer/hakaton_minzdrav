from datetime import datetime

from django.contrib.auth.models import User

from api.const import IMPORT_EXCEL_TEMPLATE_ENUM, SOURCE_ENUM, IMPORT_DATA_SET_STATUS_ENUM, SEX_ENUM
from api.models import MedDataSet, Mkb10, Patient, DoctorVariant, Doctor, AssignmentVariant, Assignment
from api.service import ImportService
import pandas as pd


class ImportExcelService(ImportService):
    HEADER_MIS_MOSCOW = [
        {
            'label': 'Номер полиса пациента*',
            'required': True
        },
        {
            'label': 'ФИО пациента',
            'required': False
        },
        {
            'label': 'Пол пациента',
            'required': False
        },
        {
            'label': 'Дата рождения пациента',
            'required': False
        },

        {
            'label': 'СНИЛС пациента',
            'required': False
        },
        {
            'label': 'Телефон пациента',
            'required': False
        },
        {
            'label': 'Номер паспорта пациента',
            'required': False
        },
        {
            'label': 'ID приема*',
            'required': True
        },
        {
            'label': 'Дата оказания услуги*',
            'required': True
        },
        {
            'label': 'ID врача*',
            'required': True
        },
        {
            'label': 'ФИО врача',
            'required': False
        },
        {
            'label': 'Должность',
            'required': False
        },
        {
            'label': 'Код МКБ-10*',
            'required': True
        },
        {
            'label': 'Назначения*',
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
        return list(map(lambda x: x['label'], item_header_list))

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

                if column_label == 'Код МКБ-10*':
                    try:
                        Mkb10.objects.get(code=row_val)
                    except Mkb10.DoesNotExist:
                        check_data_error_list.append({
                            'row': index_row,
                            'error': f'Неизвестный код МКБ10: "{row_val}"'
                        })

            if error_column_list:
                check_data_error_list.append({
                    'row': index_row,
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

    def update_data_moscow_mis(self, excel_ds, source: SOURCE_ENUM):
        for row in excel_ds:
            # добавляем пациента
            patient_data = {}
            patient_data['polis'] = row['Номер полиса пациента*']

            if not pd.isnull(row['ФИО пациента']) and row['ФИО пациента']:
                patient_data['fio'] = row['ФИО пациента']

            if not pd.isnull(row['Пол пациента']) and row['Пол пациента']:
                if row['Пол пациента'] == 'Муж':
                    patient_data['sex'] = SEX_ENUM.MALE
                if row['Пол пациента'] == 'Жен':
                    patient_data['sex'] = SEX_ENUM.FEMALE

            if not pd.isnull(row['Дата рождения пациента']) and row['Дата рождения пациента']:
                try:
                    patient_data['date_birth'] = datetime.strptime(row['Дата рождения пациента'], "%d.%m.%Y").date()
                except Exception:
                    patient_data['date_birth'] = None

            if not pd.isnull(row['СНИЛС пациента']) and row['СНИЛС пациента']:
                patient_data['snils'] = row['СНИЛС пациента']

            if  not pd.isnull(row['Телефон пациента']) and row['Телефон пациента']:
                patient_data['phone'] = row['Телефон пациента']

            patient, is_created = Patient.objects.update_or_create(
                polis=row['Номер полиса пациента*'],
                defaults=patient_data
            )

            # добавляем врача
            doctor_data = {
                'source':SOURCE_ENUM.MSK_MIS,
                'source_fio':None,
                'source_specialization':None,
            }

            if  not pd.isnull(row['ФИО врача']) and row['ФИО врача']:
                doctor_data['source_fio'] = row['ФИО врача']

            if not pd.isnull(row['ID врача*']) and row['ID врача*']:
                doctor_data['source_id'] = row['ID врача*']

            if not pd.isnull(row['Должность']) and row['Должность']:
                doctor_data['source_specialization'] = row['Должность']

            doctor_variant, is_created = DoctorVariant.objects.get_or_create(
                source_id=row['ID врача*'],
                source=SOURCE_ENUM.MSK_MIS,
                defaults=doctor_data
            )

            if not doctor_variant.doctor:
                doctor = Doctor.objects.create(
                    fio=doctor_data['source_fio'],
                    specialization=doctor_data['source_specialization'],
                )
                doctor_variant.doctor = doctor
                doctor_variant.save()

            # наполнение базы назначений
            assignment_str = row['Назначения*']
            assignment_str = assignment_str.replace(';', '\n')
            assignment_list = assignment_str.split('\n')
            for assignment_name in assignment_list:
                if assignment_name:
                    assignment_variant, is_created = AssignmentVariant.objects.get_or_create(
                        name=assignment_name,
                        source=SOURCE_ENUM.MSK_MIS,
                        defaults={
                            'name':assignment_name,
                            'source':SOURCE_ENUM.MSK_MIS
                        }
                    )
                    if not assignment_variant.assignment:
                        assignment = Assignment.objects.create(
                            name=assignment_name
                        )
                        assignment_variant.assignment = assignment
                        assignment_variant.save()






    def check_assignment(self, excel_ds, source: SOURCE_ENUM, excel_template: IMPORT_EXCEL_TEMPLATE_ENUM):
        """
        проверка назначений и заполнения справочных таблиц
        """
        if excel_template == IMPORT_EXCEL_TEMPLATE_ENUM.MIS_MOSCOW:
            return self.check_moscow_mis(excel_ds, source)

    def import_excel(self, excel_file, user: User, source: SOURCE_ENUM,
                     excel_template: IMPORT_EXCEL_TEMPLATE_ENUM = IMPORT_EXCEL_TEMPLATE_ENUM.MIS_MOSCOW,
                     data_set_name=''):
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
            med_data_set.import_status = IMPORT_DATA_SET_STATUS_ENUM.ERROR_FILE
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

        if excel_template == IMPORT_EXCEL_TEMPLATE_ENUM.MIS_MOSCOW:
            self.update_data_moscow_mis(excel_ds=excel_ds, source=source)

        # self.check_assignment(excel_ds=excel_ds, source=source, excel_template=excel_template)

        med_data_set.import_status = IMPORT_DATA_SET_STATUS_ENUM.SUCCESS
        med_data_set.save()
        return med_data_set
