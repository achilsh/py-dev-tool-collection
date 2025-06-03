from fastapi import APIRouter, Depends 
from app.schemas.demo_user import UserRequest
from app.schemas.demo_user import UserResponse
from app.services.get_info import UserInfo
from app.schemas.demo_user import StudentResponse
from app.schemas.demo_user import StudentRequest
from app.databases.user_op import create_user
from app.databases.user_op import get_user
from app.databases.user_op import get_user_one
from app.databases.user_op import get_fields
from app.databases.user_op import *
from app.core.log import logger


router = APIRouter() 

@router.post("/get_info", response_model=UserResponse)
async def getInfo(req: UserRequest):
    demo = UserInfo()
    ## 创建一条记录
    # user = await create_user(username=req.username, email=req.email)
    # logger.info(f"user: {user}")

    ## 查询一条记录
    user= await get_user(id=1)
    logger.info(f"get user id:{1}, value: {user}")
    #

    ###
    user = await get_user_one(id=1)
    logger.info(f"get first: {user}")
    
    
    ret = await update_value(id=1, email="adfad")
    logger.info(f"ret: {ret}")

    items = await get_fields(id=1)
    logger.info(f"items: {items}")
    
    
    return demo.get_info(req)

    pass


@router.post("/stud_info", response_model = StudentResponse, response_model_exclude_none=True)
def stud_info(req: StudentRequest):
    pass