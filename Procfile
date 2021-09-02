web: gunicorn linkshort.wsgi --log-file -
celery: celery -A linkshort worker -l INFO --pool=solo
