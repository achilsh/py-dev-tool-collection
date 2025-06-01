from fastapi import APIRouter, Depends 
from app.schemas.demo_user import UserRequest
from app.schemas.demo_user import UserResponse
from app.services.get_info import UserInfo
from app.schemas.demo_user import StudentResponse
from app.schemas.demo_user import StudentRequest


router = APIRouter() 

@router.post("/get_info", response_model=UserResponse)
def getInfo(req: UserRequest):
    demo = UserInfo()
    return demo.get_info(req)
    pass


@router.post("/stud_info", response_model = StudentResponse, response_model_exclude_none=True)
def stud_info(req: StudentRequest):
    pass