import os

import pydantic_settings

BASE_DIR = os.path.dirname(__file__)


class Settings(pydantic_settings.BaseSettings):
    SAUCEDEMO_URL: str = "https://www.saucedemo.com"
    SAUCEDEMO_LOGIN: str
    SAUCEDEMO_PASSWORD: str
    REQRES_IN_URL: str = "https://reqres.in"


settings = Settings(_env_file=os.path.join(BASE_DIR, ".env"))
