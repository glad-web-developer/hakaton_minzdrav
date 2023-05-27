from django.contrib.auth.models import User
from django.db import models

from api.const import ROLE_ENUM
from api.models import MedOrganization


class MedUser(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        db_table = 'med_user'

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.PROTECT, related_name='polzovatel', unique=True)
    med_organiizaciya = models.ForeignKey(MedOrganization, verbose_name='Медицинская организация',
                                          on_delete=models.PROTECT, null=True, blank=True)
    fio = models.CharField(verbose_name='ФИО', max_length=255)
    role = models.IntegerField(verbose_name='Роль', choices=ROLE_ENUM.choices)

    def __str__(self):
        return f'{self.fio} ({self.med_organiizaciya.name if self.med_organiizaciya else ""})'

