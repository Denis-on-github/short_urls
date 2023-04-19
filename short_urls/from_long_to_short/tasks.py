from __future__ import absolute_import, unicode_literals
from celery import shared_task
from short_urls.celery import app
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from .models import *
import time

logger = get_task_logger(__name__)

@app.task
def test():
    print('ТАСКА РАБОТАЕТ! УРА!')
    logger.info('Наконец-то заработало...')
    #Users.objects.get_or_create(user_ip=time.time)
    return 'Нужен ретерн?'

@app.task
def test_2():
    print('ВТОРАЯ ТАСКА ЗАВЕЛАСЬ, ЧТО С ПЕРВОЙ?')
    return 'Не знаю для чего он нужен'

@shared_task
def test_3():
    print('ТРЕТЬЯ ТАСКА ТОЖЕ РАБОТАЕТ!')
    return 'Зачем нужен ретерн, все еще не понимаю'

# @shared_task
# def add(x, y):
#     return x + y
#
# @shared_task
# def mul(x, y):
#     return x * y
#
# @shared_task
# def xsum(numbers):
#     return sum(numbers)