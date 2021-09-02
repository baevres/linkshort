web: gunicorn linkshort.wsgi --log-file -
worker: celery -A linkshort.celery worker -B --loglevel=info
