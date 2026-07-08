"""
Application configuration.

Purpose:
    Centralize all runtime configuration for the application.

Responsibilities:
    - Load configuration
    - Validate configuration
    - Provide configuration to the rest of the application

This module acts as the Single Source of Truth (SSOT)
for runtime application settings.
"""

from pathlib import Path
import os
import sys

from dotenv import load_dotenv

# Locate the project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Load environment variables from the project's .env file
load_dotenv(BASE_DIR / ".env")

APP_NAME = os.getenv("APP_NAME","linkedin tech agent")
APP_ENV = os.getenv("APP_ENV","development")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

LOG_LEVEL = os.getenv("LOG_LEVEL","INFO")

REQUIRED_SETTINGS={
    "OPENAI_API_KEY":OPENAI_API_KEY,
    "OPENAI_MODEL":OPENAI_MODEL
    }


def validate_required_settings(required_settings: dict) -> None:
    """
    Validate that all required settings are present.
    """
    missing_settings=[]
    for setting_name, setting_value in required_settings.items():
        if not setting_value:
            missing_settings.append(setting_name)
        
    if missing_settings:
        #print("Required settings are missing:{0}".format(missing_settings))
        print("\nConfiguration Error")
        print("-" * 50)
        print("Missing required environment variables:\n")
        for setting in missing_settings:
            print(f"  - {setting}")
        print("\nPlease update your .env file and restart the application.")
        sys.exit(1)
    print("Configuration validation completed successfully.")

