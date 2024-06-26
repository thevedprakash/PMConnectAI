import pathlib
import textwrap
import os
# pip3 install -U google-generativeai requests python-dotenv
import google.generativeai as genai


model = genai.GenerativeModel('gemini-pro')

GOOGLE_API_KEY =  os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# https://github.com/google-gemini/generative-ai-python

def prompt():
    input="How are you doing today?"
    response = model.generate_content(input)
    print(response.text)
    return response

if __name__ == "__main__":
    prompt()