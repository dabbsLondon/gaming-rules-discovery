"""Configuration utilities."""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    database_url: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres/postgres")


def get_settings() -> Settings:
    return Settings()
