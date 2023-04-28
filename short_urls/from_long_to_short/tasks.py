from celery import shared_task

from from_long_to_short.models import Users
from from_long_to_short.views import redis_instance
from short_urls.celery import app

@shared_task
'''По факту эта таска не работает, все наши переменные пустые,
потому что изначальный запрос неправильный'''
def check_user_activities():
    query_set = Users.objects.filter(user_ip__in=redis_instance.keys())
    print('ВСЕ КЛЮЧИ РЕДИС', redis_instance.keys())
    print('А ЭТО ПРОСТО КВЕРИ СЭТ', query_set)
    unactive_users = [user for user in query_set if redis_instance.get(str(user.user_ip)) != 'b\'''(nil)']
    print('ЭТО НАШИ НЕАКТИВНЫЕ', unactive_users)
    active_users = [user for user in query_set if redis_instance.get(str(user.user_ip)) == 'b\'''(nil)']
    print('ЭТО НАШИ АКТИВНЫЕ', active_users)

# @shared_task
# def check_user_activities():
#     query_set = Users.objects.all()
#     all_users = [user.user_ip for user in query_set]
#     print(all_users)
#     for user in all_users:
#         if redis_instance.get(user) == '(nil)':
#             Users.delete(user)

@app.task
def test_task():
    print('test_task is working!')