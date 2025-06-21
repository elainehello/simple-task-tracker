import time
from celery import Celery
from celery import shared_task

celery_app = Celery (
    "tasks",
    broker = "redis://localhost:6379/0",
    backend = "redis://localhost:6379/0"
)

@shared_task
def simulate_task(task_id: str):
    for i in range(5):
        print(f"[{task_id}] Step {i + 1}/5")
        time.sleep(1)
    print(f"[{task_id}] Task complete")