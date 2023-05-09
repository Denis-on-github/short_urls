FROM python:3.11.0

ENV PYTHONUNBUFFERED 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /test_task_short_urls/
COPY short_urls /test_task_short_urls/short_urls
WORKDIR /test_task_short_urls
EXPOSE 8000

RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /test_task_short_urls/short_urls