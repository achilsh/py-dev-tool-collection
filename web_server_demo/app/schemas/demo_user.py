
from pydantic  import BaseModel 

class UserRequest(BaseModel):
    id: int  
    username: str 
    email: str

class UserResponse(BaseModel):
    code: int
    message: str 
    data: str