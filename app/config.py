import os
from dotenv import load_dotenv

env_file = ".env.test" if os.getenv("ENV") == "test" else ".env"
load_dotenv(env_file)

class Settings:
    ENV: str = os.getenv("ENV", "development")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/dbname")

settings = Settings()