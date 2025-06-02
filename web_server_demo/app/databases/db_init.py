

from tortoise import Tortoise, fields, models, run_async
from app.core.config import settings

import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from routers import router as users_router

from examples.fastapi.config import register_orm
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise, tortoise_exception_handlers

async def init_db():
    await  Tortoise.init (
        userPasswd = settings.DB_USER +":" + settings.DB_PASSWORD
        db_url='mysql://' + userPasswd + '@' + settings.DATABASE_URL + '/tortoise_demo?asyncmy=true',
        modules={'models': ['app.models']},
        timezone='Asia/Shanghai',
        # 连接池配置
        connection_params={
            'maxsize': 20,  # 最大连接数
            'minsize': 5,    # 最小连接数
            'connect_timeout': 30,  # 连接超时
            'charset': 'utf8mb4',   # 字符集
        }
    )
    # 生成数据库表，不存在运行上面 init()的规则
    await Tortoise.generate_schemas(safe=True) 
    print("Database initialized")