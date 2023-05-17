from fastapi import FastAPI, Body
import uvicorn
import pandas as pd

app = FastAPI()

# @app.put("/putXml")
# def send_xml(data=Body(None)):
#     return {"data":data}


@app.get("/xml")
def get_body(data=Body(None)):

    xml_string = data
    df = pd.read_xml(xml_string, xpath="/request")

    name = df.loc[0, "name"]
    age = str(df.loc[0, "age"])
    gender = df.loc[0, "gender"]

    return {
        "name": name,
        "age": age,
        "gender": gender
    }


if __name__ == "__main__":
    uvicorn.run("xml_demo:app", host="127.0.0.1", port=8080, reload=True)
