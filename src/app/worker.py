import os
from celery import Celery

celery_app = Celery(
    "worker",
    broker=os.environ["REDIS_URL"],
    backend=os.environ["REDIS_URL"],
    include=["app"],
)
