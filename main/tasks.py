import datetime
from linkshort.celery import app
from django.utils import timezone

from .models import *


@app.task(bind=True)
def delete_url(self):
    now = timezone.make_aware(datetime.datetime.now(), timezone.get_default_timezone())
    urls = ShortLink.objects.filter(end_time__gte=now)
    if urls:
        urls.delete(hour='*', minute=0)
    return
