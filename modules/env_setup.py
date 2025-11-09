import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def env_load():
    if not api_key:
        print("No API key found.")
    elif not api_key.startswith("sk-proj-"):
        print("API key found but does not start by sk-proj-.")
    elif api_key.strip() != api_key:
        print("API key found but has spaces.")
    else:
        print("API key found!!!!")