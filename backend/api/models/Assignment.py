from django.db import models

class Assignment(models.Model):
    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'
        db_table = 'assignment'

    name = models.CharField('Название', max_length=255, unique=True)

    def __str__(self):
        return self.name