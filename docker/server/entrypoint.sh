#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

echo "Your auth token"
python manage.py adduser
export DEBUG=False
gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
#python manage.py runserver 0.0.0.0:8000