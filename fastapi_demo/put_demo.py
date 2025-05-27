from fastapi import FastAPI 
from pydantic import BaseModel 
from typing import Union

app = FastAPI() 

class Item(BaseModel):
    name: str ### 变量名 :  类型提示
    price: float  ### 变量名 :  类型提示
    is_offer: Union[bool, None] =None 
    
@app.get("/")
def read_root():
    return {"hello":"world"}


#  url: get http://xxx/items/xx?q=xx  其中 q 是可选
# 其中 items 是： 路径参数， 类型是  int
#  q 是查询参数


#  FastAPI 通过类型声明 自动解析请求中的数据。
@app.get("/items/{item_id}") ###
def read_item(item_id: int, q: Union[str, None]=None):
    return {"item_id": item_id, "q": q}


## put: http://xxx/items/yy
# 其中 request body: 
# {
#   "name":"", 
#   "price": 0.0,
#   "is_offer": true 
# }
# 其中 json 请求体 转换 类 
@app.put("/items/{item_id}")
def update_item(item_id: int, item:Item):
    return {"item_name": item.name, "item_id": item_id*item.price}

## 如果 代码中使用 async / await, 则使用 async def 上面函数，比如：
## async def read_item()


## 参考： https://fastapi.tiangolo.com/zh/

## 事先要安装依赖库：
# pip install fastapi
# pip install uvicorn 

# 在 fastapi_demo 目录中运行如下命令：  uvicorn put_demo:app --reload
#  其中 main 是 模块 put_demo.py 的 put_demo
#  其中 app 是 是 创建了一个 FastAPI 应用实例；eg: app = FastAPI()

## 在浏览器上输入：http://127.0.0.1:8000/items/10?q=achilsh

## http://127.0.0.1:8000/docs  或者 http://127.0.0.1:8000/redoc 是接口文档