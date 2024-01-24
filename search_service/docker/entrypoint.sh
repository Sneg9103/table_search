#!/bin/sh
set -e 

export PYTHONPATH=/var/www/html:$PYTHONPATH
python3 /var/www/html/docker/db_healthcheck.py
cd /var/www/html
python3 manage.py migrate
python3 manage.py collectstatic --noinput

# Check and create superuser if necessary
if [ -n "${DJANGO_SUPERUSER_USERNAME}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD}" ] && [ -n "${DJANGO_SUPERUSER_EMAIL}" ]; then
    python3 manage.py shell < /var/www/html/docker/check_superusers.py
fi

# Start ASGI or WSGI server
if [ "$1" = 'asgi' ]; then
    exec daphne -u ./tmp/daphne.sock config.asgi:application
else
    exec gunicorn config.wsgi:application -w 2 -b :8000 --reload --timeout 300
fi