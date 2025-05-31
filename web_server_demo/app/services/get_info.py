from app.schemas.demo_user import UserRequest, UserResponse
from app.core.log import logger
class UserInfo():
    def __init__(self):
        pass
    def get_info(self, req: UserRequest)->UserResponse:
        logger.info(f"call get_info: {req}") 
        ret = UserResponse(code=100,message="get info response", data="this is response data.")
        return ret