import uvicorn
from fastapi import FastAPI,Header,Body,Form
from fastapi.responses import JSONResponse,HTMLResponse,FileResponse

app = FastAPI()

# @app.post("/login")
# def login():
#     return {"msg":"login success"}
@app.api_route("/login",methods=["GET","POST","PUT"])
def login():
    return {"msg","login success"}

@app.get("/token")
def get_token(token=Header(None)):
    return {"token":token}

@app.get("/body")
def get_body(username=Form(None),password=Form(None)):
    return {"body":{
        "username":username,
        "password":password
    }}

@app.get("/pages")
def get_pages(name):
    
    content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body style="display:flex;justify-content:center;align-items:center;height:100vh">
            <h1>你好! {name}！</h1>
        </body>
        </html>
    """
    return HTMLResponse(content=content)


@app.get("/avatar")
def get_avatar():
    
    avatar_path = "./static/image.png"
    return FileResponse(avatar_path,filename="myfile.png") #? 指定给到用户的文件名

if __name__ == "__main__":
    uvicorn.run("main02:app", host="172.18.1.35",port=17676, reload=True)