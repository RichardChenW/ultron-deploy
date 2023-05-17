from fastapi import APIRouter

app01 = APIRouter()


@app01.get("/predict")
def predict():
    return {"message": "Hello World"}
