import os
from celery import Celery
from celery.schedules import crontab

from .settings import BASE_REDIS_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linkshort.settings')

app = Celery('linkshort')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-urls-every-hour': {
        'task': 'main.tasks.delete_url',
        'schedule': crontab(hour='*', minute=0),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}