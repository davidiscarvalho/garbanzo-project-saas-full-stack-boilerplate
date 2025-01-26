# ./core/config.py

from pydantic_settings import BaseSettings
from typing import Optional

if __name__ == "__main__":
    from pathlib import Path
    import os
    # Resolve the .env file path
    print("Current Working Directory:", os.getcwd())
    env_path = Path("../.env").resolve()
    print("Resolved .env Path:", env_path)
    print("Does the file exist?", env_path.exists())


class Settings(BaseSettings):
    ENV: str = "dev"  # Default to development
    SQLITE_DB: Optional[str] = None
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    DB_ECHO: bool = False
    SECRET_KEY_JWT: str

    class Config:
        extra = "ignore"  # Ignore extra fields

    @property
    def DATABASE_URL(self) -> str:
        """
        Automatically determine the database URL based on the environment.
        """
        if self.ENV == "prod":
            return (
                f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )
        return self.SQLITE_DB

settings = Settings(_env_file="../.env", _env_file_encoding="utf-8")
# print(settings)
# print("DATABASE_URL: ",settings.DATABASE_URL)

if __name__ != "__main__":
    print("\n***********************************")
    if settings.ENV == "prod":
        print("*** Running in PRODUCTION mode ***")
    else:
        print("*** Running in DEVELOPMENT mode ***")
    print("***********************************\n")





