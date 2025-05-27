
from pydantic import BaseModel  ## 请求body的模型
from typing import Optional ##可选参数或者可选字段
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings  ## 读取 .env 环境变量配置文件


## BaseModel 作为模型的基类。
class demoPydantic(BaseModel): 
    name: str 
    dataInputFlag: int|bool 
    optInput: Optional[str]  ## 可选字段
    age: int = 10 ## 添加默认值
    



## 模型嵌套
class EmbeddingPydantic(BaseModel): 
    item: demoPydantic
    
def callDemoPydantic(): 
    ## 如何对 继承 BaseModel 的类对象初始化？
    #  把每个字段的字段名和值对 传入类的构造函数中。
    item = demoPydantic(
        name="this is demo",
        dataInputFlag= True, 
        optInput="this is opt"
    )
    
    dictVal = {
        "name": "aaa",
        "dataInputFlag": False, 
        "optInput": "bbbb"
    }
    ## 把 字典 的值 decode 后作为 key, value 对传给构造函数中。
    item1 = demoPydantic(**dictVal)
    print(item1.model_dump())

    item2 = EmbeddingPydantic(
        item = demoPydantic(
        name="this is demo",
        dataInputFlag= True, 
        optInput="this is opt"
    ))
    
    
## 配置文件读取，eg： .env 环境变量 
class  Setting(BaseSettings):
    app_name: str   # 必填字段，必须来自环境变量或 .env
    debug: bool = False ## 携带默认值 
    port: int = 8080 ## 携带默认值 
    
    class Config:
        env_file = ".env"

def callSetting():
    s =  Setting() 
    print(s.app_name)
    print(s.model_dump())

if __name__ == '__main__': 
    callDemoPydantic()
    callSetting()