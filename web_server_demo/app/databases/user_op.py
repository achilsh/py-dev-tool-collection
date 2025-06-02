
from app.models.user import UserModel
async def create_user(username: str, email: str):
    user = await UserModel.Create(name=username, email=email)
    return user

async def get_user(id: int):
    user = await UserModel.get(id=id)
    return user

        