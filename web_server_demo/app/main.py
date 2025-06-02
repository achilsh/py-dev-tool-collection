from  fastapi  import FastAPI   
from app.api.v1 import demo_user
from app.core.config import Settings
from app.core.config import settings
from app.core.config import register_orm
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise, tortoise_exception_handlers





@asynccontextmanager
async def lifespan_test(app: FastAPI) -> AsyncGenerator[None, None]:
    config = generate_config(
        settings.DATABASE_URL,
        app_modules={"models": ["app.models"]},
        testing=True,
        connection_label="models",
    )
    async with RegisterTortoise(
        app=app,
        config=config,
        generate_schemas=True,
        _create_db=True,
    ):
        # db connected
        yield
        # app teardown
    # db connections closed
    await Tortoise._drop_databases()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    if getattr(app.state, "testing", None):
        async with lifespan_test(app) as _:
            yield
    else:
        # app startup
        async with register_orm(app, add_exception_handlers=True):
            # db connected
            yield
            # app teardown
        # db connections closed
app = FastAPI(
    title="demo server on python",
    lifespan=lifespan,
    exception_handlers=tortoise_exception_handlers(),
)

print("load models: ", Tortoise.apps)

# print(Settings().model_dump())
app.include_router(demo_user.router, prefix=settings.API_PREFIX)
