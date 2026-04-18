import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "The Sandras API"
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb+srv://HK_Digiverse:HK%40Digiverse%40123@cluster0.lcbyqbq.mongodb.net/the_sandras?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "the_sandras")

settings = Settings()
