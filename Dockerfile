FROM python:3-alpine

ARG VERSION=dev
ENV VERSION=$VERSION

COPY . /app
WORKDIR /app

ENV GERRIT_URL "https://gerrit.aospa.co"
ENV CACHE_DEFAULT_TIMEOUT "3600"
ENV CACHE_TYPE "simple"
ENV CACHE_REDIS_HOST "redis"
ENV CACHE_REDIS_DB 4
ENV UPSTREAM_URL ""
ENV DOWNLOAD_BASE_URL "https://updates.aospa.co"
ENV FLASK_APP "app.py"

RUN pip install -r requirements.txt

EXPOSE 8080

ENV prometheus_multiproc_dir=/app/metrics/

CMD gunicorn -b 0.0.0.0:8080 -w 8 app:app
