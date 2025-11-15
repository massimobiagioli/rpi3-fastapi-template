import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(__name__)
celery_app.conf.broker_url = os.environ.get("REDIS_URL", "redis://localhost:6379")
celery_app.conf.result_backend = os.environ.get("REDIS_URL", "redis://localhost:6379")
celery_app.conf.timezone = 'UTC'


@celery_app.task
def test_worker():
    return {"status": "success", "message": "Worker is running"}