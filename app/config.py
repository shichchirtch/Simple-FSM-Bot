from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        # a = f"postgresql+asyncpg://postgres:postgres@postgres_main:5432/b_base"
    model_config = SettingsConfigDict(env_file="../env/main.env", env_file_encoding='utf-8')
    #  env_file="../env/main.env" - означает выйди в вышестоящую директорию,
    #  зайди в папку env, читай файл main.env


settings = Settings()
