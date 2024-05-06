web: gunicorn webinar.wsgi:application

release: python manage.py migrate --no-input

worker: python manage.py rqworker default
