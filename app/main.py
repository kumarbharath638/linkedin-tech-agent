"""
Application entry point.

Responsible for orchestrating the application startup lifecycle.
"""

from app.config import settings
from app.llm.mock_llm import MockLLM
from app.llm.base_llm import BaseLLM
from app.services.linkedin_service import LinkedInService
from app.prompts.linkedin_prompt import generate_post_prompt


def start_up():
    print("=" * 60)
    print(f"Starting {settings.APP_NAME}")
    print("=" * 60)

def validation_setting():
    settings.validate_required_settings(settings.REQUIRED_SETTINGS)
    print("\nApplication Startup Information")
    print("-" * 60)
    print(f"Application Name : {settings.APP_NAME}")
    print(f"Environment      : {settings.APP_ENV}")
    print(f"Log Level        : {settings.LOG_LEVEL}")
    print("\nApplication is ready.")

def create_dependencies():
    llm=MockLLM()
    linkedin_service=LinkedInService(llm)
    return linkedin_service

def run_application(linkedin_service):
    topic = "Artificial Intelligence"
    response=linkedin_service.generate_post(topic)
    print("\nGenerated LinkedIn Post")
    print("-" * 60)
    print(response)

def shutdown():
    print("Application completed successfully")


def main():
    start_up()
    validation_setting()
    linkedin_service=create_dependencies()
    run_application(linkedin_service)
    shutdown()

if __name__ == "__main__":
    main()