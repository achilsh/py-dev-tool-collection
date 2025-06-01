
from pydantic  import BaseModel 
from typing import List
from typing import Optional

class UserRequest(BaseModel):
    id: int  
    username: str 
    email: str

class UserResponse(BaseModel):
    code: int
    message: str 
    data: str



class StudItem(BaseModel):
    name: str
    age: int
# 参数是 Optional
class StudentRequest(BaseModel):
    Students: Optional[List[StudItem]] =None


class StudRepItem(BaseModel):
    Value: str
class StudentResponse(BaseModel):
    Result: Optional[List[StudRepItem]] = None

    class Config:
        # 当字段为 None 时不包含在序列化结果中
        exclude_none = True
