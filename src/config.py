"""Application configuration loaded from environment variables."""

import os

from dotenv import load_dotenv

load_dotenv()


def get_gemini_api_key() -> str:
    """Return the Gemini API key or an empty string when it is unavailable."""
    return os.getenv("GEMINI_API_KEY", "").strip()


def get_model_name() -> str:
    """Return the configured Gemini model name."""
    return os.getenv("MODEL_NAME", "gemini-3.5-flash").strip()