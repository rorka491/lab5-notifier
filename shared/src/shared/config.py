from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitMQSettings(BaseSettings):
    url: str = "amqp://guest:guest@localhost:5672/"

    model_config = SettingsConfigDict(env_prefix="RABBITMQ_", env_file=".env", extra="ignore")


class PostgresSettings(BaseSettings):
    url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/lab5"

    model_config = SettingsConfigDict(env_prefix="POSTGRES_", env_file=".env", extra="ignore")



pg_settings = PostgresSettings()
rabbit_settings = RabbitMQSettings()