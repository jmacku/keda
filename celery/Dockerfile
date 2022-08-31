FROM python:3.10-slim

WORKDIR /app


RUN pip install \
  "celery[redis]" \
  flask structlog \
  psycopg2-binary \
  sqlalchemy \
  celery-redis-sentinel \
  greenlet

COPY app.py .

EXPOSE 5000