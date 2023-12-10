import time
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# 查询参数 q 的类型为 str，默认值为 None，因此它是可选的。
@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        time.sleep(10)
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.get("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
