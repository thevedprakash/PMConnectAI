
import os
from dotenv import load_dotenv

# Load environment variables from the .env file into the application's environment.
load_dotenv()

class Config:
    # Class to hold configuration constants and environment variables.

    # Slack API token for interacting with Slack APIs.
    SLACK_TOKEN = os.getenv("SLACK_TOKEN")
    # Version of the Google Gemini API being used.
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # UUID for the Calendly event type, used for scheduling links.
    CALENDLY_EVENT_UUID = os.getenv("CALENDLY_EVENT_UUID")
    # API key for Calendly integration.
    CALENDLY_API_KEY = os.getenv("CALENDLY_API_KEY")

    # API key for LangChain Smith services.
    LANGCHAIN_SMITH_API_KEY = os.getenv("LANGCHAIN_SMITH_API_KEY")
    # Fixed endpoint for LangChain Smith API services.
    LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com"
    # Identifier for the project in LangChain services.
    LANGCHAIN_PROJECT = "PMConnect AI"
    # Enable detailed tracing for LangChain operations.
    LANGCHAIN_TRACING_V2 = "True"
