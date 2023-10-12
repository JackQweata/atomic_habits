from celery import shared_task

from main.models import Habit
from main.services import send_message_tg


@shared_task
def daily_newsletter():
    habits = Habit.objects.filter(frequency=1, user__tg_id__isnull=False)
    for item in habits:
        send_message_tg(item.user.tg_id, f'Пора выполнить {item.action} в {item.time}')


@shared_task
def weekly_newsletter():
    habits = Habit.objects.filter(frequency=7, user__tg_id__isnull=False)
    for item in habits:
        send_message_tg(item.user.tg_id, f'Пора выполнить {item.action} в {item.time}')
