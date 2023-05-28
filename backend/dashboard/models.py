from django.db import models


class Dashboard(models.Model):
    title = models.CharField(verbose_name="Название доски", max_length=255)

    def __str__(self):
        return self.title


class Widget(models.Model):
    title = models.CharField(verbose_name="Название виджета", max_length=255)
    component = models.CharField(verbose_name="Компонент", max_length=255)
    cols = models.IntegerField(verbose_name="Ширина в колонках")

    def __str__(self):
        return self.title


class WidgetCoordinates(models.Model):
    dashboard = models.ForeignKey(verbose_name='dashboard', to=Dashboard, on_delete=models.CASCADE)
    widget = models.ForeignKey(verbose_name='widget', to=Widget, on_delete=models.CASCADE)
    x = models.IntegerField(verbose_name='X')
    y = models.IntegerField(verbose_name='Y')
