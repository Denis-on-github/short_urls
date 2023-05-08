from celery import shared_task
from from_long_to_short.models import *
from from_long_to_short.views import redis_instance
from short_urls.celery import app

@shared_task
def check_user_activities():
    redis_query = redis_instance.keys()
    redis = [i.decode('utf-8') for i in redis_query]
    users_query = Users.objects.all()
    users = [user.user_ip for user in users_query]
    print(f'All active users in Redis DB: {redis}')
    print(f'All users in DB: {users}')

    for user in users:
        if user not in redis:
            print(f'This {user} is unactive for a long time, it was delete from DB.')
            Users.objects.get(user_ip=user).delete()

@app.task
def test_task():
    print('test_task is working!')