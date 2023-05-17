from fastapi import FastAPI
from api.routes.r1 import app01
import uvicorn

app = FastAPI()
app.include_router(app01, prefix="/app01", tags=["app01"])


@app.get("/")
def home():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
