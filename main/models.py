from django.db import models
from users.models import User

BLANCNULL = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=255, verbose_name='место, в котором необходимо выполнять привычку')
    time = models.TimeField(verbose_name='время, когда необходимо выполнять привычку', **BLANCNULL)
    action = models.TextField(verbose_name='Действие', **BLANCNULL)
    is_enjoyable = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, **BLANCNULL, verbose_name='связи')
    frequency = models.IntegerField(default=1, choices=[(1, 'Ежедневная'), (7, 'Еженедельная')], )
    reward = models.CharField(max_length=255, blank=True, verbose_name='награда')
    estimated_time = models.PositiveIntegerField(default=0, help_text='Время в секундах')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

