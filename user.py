from fastapi import APIRouter

user_router = APIRouter()

user_router = APIRouter(prefix="/users")


@user_router.get("/")
async def read_users():
    return {"message": "Here are the users"}
