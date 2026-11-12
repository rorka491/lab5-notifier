from pydantic_settings import BaseSettings, SettingsConfigDict


class EmailSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    email_host: str
    email_port: int
    email_username: str
    email_password: str



settings = EmailSettings() # type: ignore