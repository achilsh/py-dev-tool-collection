# Union 类型，用于支持多种数据类型的参数注解
from typing import Union  
from fastapi import FastAPI  


app = FastAPI()
@app.get("/")
def read_root():
    # 返回字典，该字典会被 FastAPI 自动转换为 JSON 格式并返回给用户
    return {"hello": "word"}  

#  请求参数： get, http://xxx/items/yy?q=xxx  其中 q 是可选参数
@app.get("/items/{item_id}")  ## item_id 是路径参数， q 是查询参数
def read_item(item_id: int, q: Union[str, None] = None): ## 或者使用  str|None = None
    return {"item_id": item_id, "q": q}


def get_full_name(firstname, secondname, age):
    y = firstname+age
    return firstname.title() + " " + secondname.title()

## 事先要安装依赖库：
# pip install fastapi
# pip install uvicorn 

# 在 fastapi_demo 目录中运行如下命令：  uvicorn main:app --reload
#  其中 main 是 模块 main.py 的 main
#  其中 app 是 是 创建了一个 FastAPI 应用实例；eg: app = FastAPI()

## 在浏览器上输入：http://127.0.0.1:8000/items/10?q=achilsh

## http://127.0.0.1:8000/docs  或者 http://127.0.0.1:8000/redoc 是接口文档
