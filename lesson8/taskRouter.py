from fastapi import FastAPI, Depends, APIRouter, HTTPException
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from fastapi.encoders import jsonable_encoder

task_router = APIRouter()


class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    description: constr(min_length=1, max_length=120)
    taskId: int
    status: str

    @field_validator('status')
    def check_status(cls, status):
        if status not in ['open', 'close']:
            raise ValueError('status error')
        return status

    @field_validator('taskId')
    def check_task(cls, taskId):
        if taskId < 0:
            raise ValueError('error')
        return taskId


def is_exist_id(id: int):
    if tasks[id] is not None:
        return True
    return False


tasks = {}


@task_router.get("/")
async def getTasks():
    return tasks
    raise HTTPException(status_code=404, detail="oops... your task didn't find")


@task_router.post("/")
async def add_task(task: Task, is_exist: bool = Depends(is_exist_id)):
    try:
        if is_exist is False:
            tasks[task.taskId] = task
        else:
            raise HTTPException(status_code=400, detail="oops... this id is already exist")
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {task.name}"


@task_router.put("/{id}", response_model=Task)
async def update_task(id: int, item: Task):
    update_item = jsonable_encoder(item)
    tasks[id] = update_item
    return update_item


@task_router.delete("/{id}")
async def delete_task(id: int):
    del tasks[id]
    return {"message": "Item deleted"}
