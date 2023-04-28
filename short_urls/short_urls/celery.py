import os
import time
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'short_urls.settings')

app = Celery('short_urls')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task
def debug_task():
    time.sleep(20)
    print('debug_task is working!')

app.conf.beat_schedule = {
    'check_user_activities': {
        'task': 'from_long_to_short.tasks.check_user_activities',
        'schedule': 30.0,
        'args': (),
    }
}