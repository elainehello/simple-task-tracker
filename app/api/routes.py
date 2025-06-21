from fastapi import APIRouter
from app.tasks.sample import simulate_task
from uuid import uuid4

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.post("/start-task")
async def start_task():
    task_id = str(uuid4()) # generate custom task ID
    simulate_task.apply_async(args=[task_id])
    return {"task_id": task_id, "status": "started"}
