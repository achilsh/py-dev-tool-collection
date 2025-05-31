from  fastapi  import FastAPI   
from app.api.v1 import demo_user
from app.core.config import Settings
from app.core.config import settings


app = FastAPI() 
print(Settings().model_dump()) 
app.include_router(demo_user.router, prefix=settings.API_PREFIX)
