web: gunicorn linkshort.wsgi --log-file -
worker: celery -A linkshort worker -l INFO --pool=solo
