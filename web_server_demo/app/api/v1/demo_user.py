from fastapi import APIRouter, Depends 
from app.schemas.demo_user import UserRequest
from app.schemas.demo_user import UserResponse
from app.services.get_info import UserInfo


router = APIRouter() 

@router.post("/get_info", response_model=UserResponse)
def getInfo(req: UserRequest):
    demo = UserInfo()
    return demo.get_info(req)
    pass 