import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    SLACK_TOKEN = os.getenv('SLACK_TOKEN')
    GEMINI_PRO_API_KEY = os.getenv('GEMINI_PRO_API_KEY')
    USER_EMAIL = os.getenv('USER_EMAIL')