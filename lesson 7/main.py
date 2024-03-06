from enum import Enum

import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, ValidationError

app = FastAPI()


class Status(str, Enum):
    open = 'open'
    closed = 'closed'


class Task(BaseModel):
    id: int
    name: constr(min_length=1, pattern='^[a-zA-Z]+$')
    description: constr(max_length=200)
    status: Status


tasks = [Task(id=1, name="Node", description="add node project DB", status=Status.open)]


@app.get("/tasks")
async def returnAllTasks():
    return tasks


@app.post("/tasks")
async def addTask(task: Task):
    try:
        task_dict = task.dict()
        tasks.append(task_dict)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return task_dict


@app.delete("/tasks/{id}")
async def deleteTask(taskId: int):
    try:

        for task in tasks:
            if task.id == id:
                tasks.remove(task)
            break

    except ValidationError as e:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return "task deleted"


@app.put("/tasks/{id}")
async def addTask(taskId: int, new_task: Task):
    try:
        i = 0
        for task in tasks:
            i = i + 1
            if task.id == id:
                task.name = new_task.name
                task.status = new_task.status
            break
    except ValidationError as e:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return new_task


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=800, reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
