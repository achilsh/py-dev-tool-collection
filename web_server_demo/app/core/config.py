import os
from functools import partial
from pydantic_settings import BaseSettings 

from tortoise.contrib.fastapi import RegisterTortoise

class Settings(BaseSettings):
    DATABASE_URL: str = "" ## 这里配置了默认值，在 .env 配置文件中可以不用配置该项。
    API_PREFIX: str 
    LOG_NAME: str
    LOGS_NUM: int
    DB_USER: str
    DB_PASSWORD: str
    DEMO_SRC_DIR: str
    DEMO_RUN_DIR: str
    TIME_ZONE: str
    class Config: 
        env_file=".env"
        env_file_encoding = 'utf-8'
        
settings = Settings()  # 全局唯一实例


# db_url = mysql://user:password@localhost:3306/db_name "mysql://" +
DBName="demo_db"
dbUrl = "mysql://" +  settings.DB_USER + ":" + settings.DB_PASSWORD + "@" + settings.DATABASE_URL+"/" + DBName
register_orm = partial(
    RegisterTortoise,
    db_url= dbUrl,
    modules={"models": ["app.models"]},
    generate_schemas=True,
)
