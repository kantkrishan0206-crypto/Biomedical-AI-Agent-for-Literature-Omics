from __future__ import annotations

from functools import lru_cache
from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", ".env.local"), extra="ignore")

    environment: str = Field(default="local", alias="ENVIRONMENT")
    app_name: str = "Biomedical AI Agent for Literature + Omics"
    app_owner_email: str = Field(default="kantkrishan0206@gmail.com", alias="APP_OWNER_EMAIL")
    database_url: str = Field(default="sqlite+aiosqlite:///./biomedical_ai_local.db", alias="DATABASE_URL")
    database_ssl_mode: str = Field(default="prefer", alias="DATABASE_SSL_MODE")
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    qdrant_url: str = Field(default="http://localhost:6333", alias="QDRANT_URL")
    qdrant_api_key: str | None = Field(default=None, alias="QDRANT_API_KEY")
    ollama_base_url: str = Field(default="http://localhost:11434", alias="OLLAMA_BASE_URL")
    ollama_model: str = Field(default="llama3.1", alias="OLLAMA_MODEL")
    jwt_secret: str = Field(default="local-dev-change-me", alias="JWT_SECRET")
    session_secret: str = Field(default="local-session-change-me", alias="SESSION_SECRET")
    encryption_key: str = Field(default="local-encryption-key", alias="ENCRYPTION_KEY")
    upload_encryption_key: str = Field(default="local-upload-key", alias="UPLOAD_ENCRYPTION_KEY")
    telemetry_api_key: str = Field(default="local-telemetry", alias="TELEMETRY_API_KEY")
    cors_origins: str = Field(default="http://localhost:3000", alias="CORS_ORIGINS")
    single_user_dev_mode: bool = Field(default=True, alias="SINGLE_USER_DEV_MODE")
    first_admin_email: str = Field(default="kantkrishan0206@gmail.com", alias="FIRST_ADMIN_EMAIL")
    max_upload_mb: int = Field(default=512, alias="MAX_UPLOAD_MB")

    @field_validator("database_url")
    @classmethod
    def normalize_database_url(cls, value: str) -> str:
        if value.startswith("postgresql://"):
            return value.replace("postgresql://", "postgresql+asyncpg://", 1)
        return value

    @model_validator(mode="after")
    def production_requires_real_secrets(self) -> "Settings":
        if self.environment.lower() == "production":
            weak = {"local-dev-change-me", "local-session-change-me", "local-encryption-key"}
            if self.jwt_secret in weak or self.session_secret in weak or self.encryption_key in weak:
                raise ValueError("Production startup requires strong JWT, session, and encryption secrets")
        return self

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
