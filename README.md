# Dash Celery Redis Example

An example app to run a Dash application with background callbacks using a Celery job queue. Consists of 4 containers:
  - Dash application
  - Celery worker
  - Redis database
  - Flower monitoring of the Celery worker

## Requirements

  - Docker
  - Docker compose
  - .env-file with env-variable `REDIS_URL` pointing to a running Redis instance

## Docker

Build and run the containers using the following command:

```
docker compose up --build -d
```

Stop containers:

```
docker compose down
```