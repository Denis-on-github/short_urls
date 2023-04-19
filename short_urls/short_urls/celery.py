from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

from short_urls import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'short_urls.settings')

app = Celery('short_urls')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.conf.beat_schedule = {
#     'every': {
#         'task': 'short_urls.tasks.test',
#         'schedule': crontab(),
#     },
# }

@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))