import uvicorn 
from fastapi import FastAPI

app = FastAPI()

#* 添加首页
@app.get("/")
def index():
    
    """
        这是 HOME 页面的 description
    """
    
    return "This is home page"


#* 发送 JSON 数据
@app.get("/users")
def users():
    return {"name":"richard","age":18}

#* 发送图片
@app.get("/projects")
def projects():
    return [1,2,3]


if __name__ == '__main__':
    uvicorn.run(
        "main01:app",
        host = '127.0.0.1',
        port = 8080,
        reload = True,
    )