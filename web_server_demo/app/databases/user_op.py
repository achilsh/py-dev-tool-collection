
from app.models.user import UserModel
async def create_user(username: str, email: str):
    user = await UserModel.create(name=username, email=email,cardId="1111",address="hwer")
    return user

async def get_user(id: int):
    user = await UserModel.get(id=id)
    return user

async def get_user_one(id: int):
    user = await UserModel.filter(id=id).first()
    return user

async def update_value(id: int, email: str):
    ret = UserModel.filter(id=id).update(email="xxx@126.com")

async def get_fields(id: int):
    listitem = await UserModel.all().values("id","email")
    return listitem
