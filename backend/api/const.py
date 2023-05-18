from django.db import models


class ROLE_ENUM(models.IntegerChoices):
    ADMIN = 1, 'Админ'
    CHIEF_DOCTOR = 2, 'Глав. врач'
    DOCTOR = 3, 'Доктор'
    PATIENT = 4, 'Пациент'
