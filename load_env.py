from dotenv import load_dotenv
import os


def get_github_key():
    load_dotenv()
    GITHUB_TOKEN = os.getenv("GITHUB_PAT")
    return GITHUB_TOKEN
