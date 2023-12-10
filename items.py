from fastapi import APIRouter

items_router = APIRouter()

items_router = APIRouter(prefix="/items")

@items_router.get("/")
async def read_items():
    return {"message": "Here are the items"}
