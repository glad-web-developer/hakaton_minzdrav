from django.db import models


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
    ERROR_FILE = 3, 'Ошибка чтения файла'
    ERROR_STRUCTURE = 4, 'Ошибка структуры файла или запроса'
    ERROR_ACCESS = 5, 'Ошибка прав доступа'


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