from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Tasks API")

class TaskIn(BaseModel):
    title: str
    done: bool = False

class Task(TaskIn):
    id: int

_tasks: dict[int, Task] = {}
_next_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}
    #return {"status": "broken"}
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskIn):
    global _next_id
    task = Task(id=_next_id, **payload.model_dump())
    _tasks[task.id] = task
    _next_id += 1
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = _tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
