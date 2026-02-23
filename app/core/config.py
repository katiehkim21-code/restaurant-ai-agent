"""Application configuration placeholders."""

from pydantic import BaseModel


class AppSettings(BaseModel):
    """Runtime settings for the API."""

    app_name: str = "restaurant-ai-agent"
    api_version: str = "v1"


settings = AppSettings()
