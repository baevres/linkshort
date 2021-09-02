web: gunicorn linkshort.wsgi --log-file -
worker: celery -A linkshor worker -l INFO --pool=solo
