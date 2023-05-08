import os
import time
from celery import Celery
from short_urls.settings import SCHEDULE_CHECK_USERS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'short_urls.settings')

app = Celery('short_urls')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_user_activities': {
        'task': 'from_long_to_short.tasks.check_user_activities',
        'schedule': SCHEDULE_CHECK_USERS,
        'args': (),
    }
}