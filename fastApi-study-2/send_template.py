import uvicorn
from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 解析 html文件
template = Jinja2Templates("./pages")


@app.get("/")
def send_html(name:str,req:Request):
    
    TODOLIST = ["play game","do homework","go to bed"]
    
    return template.TemplateResponse(
        "index.html",  # 指定发送过去后文件的名字
        context = {
            "request":req,
            "todos":TODOLIST # 传入动态数据
        }
    ) 


@app.post("/todo")
def todo(todo=Form(None)):
    return "new list"


if __name__ == "__main__":
    uvicorn.run(
        "send_template:app",
        host="172.18.1.35",
        port=17676,
        reload=True
    )
