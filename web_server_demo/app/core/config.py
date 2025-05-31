from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    DATABASE_URL: str = "" ## 这里配置了默认值，在 .env 配置文件中可以不用配置该项。
    API_PREFIX: str 
    LOG_NAME: str
    LOGS_NUM: int

    class Config: 
        env_file=".env"
        env_file_encoding = 'utf-8'
        
settings = Settings()  # 全局唯一实例