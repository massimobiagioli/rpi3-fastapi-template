from fastapi import FastAPI
from app.worker import test_worker

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test-worker")
async def test_worker_endpoint():
    task = test_worker.delay()
    return {"task_id": task.id, "status": "Task submitted"}