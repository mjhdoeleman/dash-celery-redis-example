# Dash Celery Redis Example

An example setup to run a containerized Dash application with background callbacks using a Celery job queue. Consists of 4 containers:
- Dash application
- Celery worker
- Redis database
- Flower monitoring of the Celery worker

## Requirements

- Docker
- Docker compose
- .env-file with env-variable `REDIS_URL` pointing to a running Redis instance

## Deployment

Build and run the containers using the following command:

```
docker compose up --build -d
```

- Dash Application: http://localhost:8050/
- Celery Monitoring with Flower ([see docs](https://flower.readthedocs.io/en/latest/)): http://localhost:5555/

Stop containers:

```
docker compose down
```