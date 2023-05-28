from django.db import models

from core.settings import MEDIA_URL, STATIC_URL


class ROLE_ENUM(models.IntegerChoices):
    ADMIN = 1, 'Админ'
    CHIEF_DOCTOR = 2, 'Глав. врач'
    DOCTOR = 3, 'Доктор'
    PATIENT = 4, 'Пациент'
    INURABCE = 5, 'Соц. страх'

class SOURCE_ENUM(models.IntegerChoices):
    MSK_MIS = 1, 'МИС Москвы'

class IMPORT_DATA_SET_STATUS_ENUM(models.IntegerChoices):
    SUCCESS = 1, 'Успешный импорт'
    WARNING = 2, 'Не все записи импортированы'
    ERROR_FILE = 3, 'Ошибка чтения файла или файл не является Excel'
    ERROR_STRUCTURE = 4, 'Ошибка структуры файла или запроса'
    ERROR_REQUIRED = 5, 'Ошибка заполнения обязательных полей'


class IMPORT_DATA_SET_DETAIL_STATUS_ENUM(models.IntegerChoices):
    SUCCESS = 1, 'Успешный импорт'
    WARNING = 2, 'Предупреждение'
    ERROR = 3, 'Ошибка'

class SEX_ENUM(models.IntegerChoices):
    MALE = 1, 'Мужской'
    FEMALE = 2, 'Женский'

class ASSIGNMENT_STATUS_ENUM(models.IntegerChoices):
    ACCEPTABLE = 1, 'Допустимое назначение'
    INVALID_ACCEPTABLE = 2, 'Недопустимое назначение'


class IMPORT_EXCEL_TEMPLATE_ENUM(models.TextChoices):
    MIS_MOSCOW = 'mis_moscow', 'МИС Москвы'

    @staticmethod
    def get_path(template_name):
        # условимся что для МИС Москвы такой формат данных
        if template_name == IMPORT_EXCEL_TEMPLATE_ENUM.MIS_MOSCOW:
            return STATIC_URL + 'dataset_to_import.xlsx'