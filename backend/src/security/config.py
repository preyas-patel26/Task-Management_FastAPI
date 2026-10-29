from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_URI : str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRY_MINUTES : int = 30
    
    model_config = SettingsConfigDict(
        env_file = ".env",
        case_sensitive = False
    )
settings = Settings()