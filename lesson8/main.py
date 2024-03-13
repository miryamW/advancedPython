import uvicorn
from fastapi import FastAPI, HTTPException
from taskRouter import task_router
from userRouter import user_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.include_router(task_router, prefix='/tasks')
app.include_router(user_router, prefix='/users')
app.mount("/static", StaticFiles(directory="static"), name="static")



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
