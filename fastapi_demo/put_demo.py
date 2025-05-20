from fastapi import FastAPI 
from pydantic import BaseModel 
from typing import Union

app = FastAPI() 

class Item(BaseModel):
    name: str 
    price: float 
    is_offer: Union[bool, None] =None 
    
@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return {"item_name": item.name, "item_id": item_id*item.price}

## 如果 代码中使用 async / await, 则使用 async def 上面函数，比如：
## async def read_item()


## 参考： https://fastapi.tiangolo.com/zh/