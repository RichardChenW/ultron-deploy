import uvicorn
from fastapi import FastAPI
import joblib
from typing import List
import os


app = FastAPI(
    title="Ultron Prediction Model API",
    description="A simple API that use LogisticRegression model to predict the ultron lead",
    version="0.1",
)

current_dir = os.path.dirname(__file__)
with open(current_dir+"/model/model.pkl", "rb") as f:
    model = joblib.load(f)

@app.get("/number")
def predict(request: int):
    """
        接口说明：预测接口
    """
    model_data = [request]
    prediction = model.predict([model_data])
    return {"prediction": prediction[0]}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
