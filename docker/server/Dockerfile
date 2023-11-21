FROM python:3.9

WORKDIR /app

COPY ./backend/requirements.txt /app/requirements.txt

RUN pip install gunicorn
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./docker /app/docker
COPY ./backend /app/backend

RUN chmod +x /app/docker/server/entrypoint.sh