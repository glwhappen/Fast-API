from fastapi import FastAPI
from user import user_router
from items import items_router
from other import other_router

app = FastAPI()


# 将用户和项目的路由添加到主应用
app.include_router(user_router)
app.include_router(items_router)
app.include_router(other_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}