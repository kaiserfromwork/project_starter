from dotenv import load_dotenv
import os


def get_github_key() -> str | None:
    """
    Imports environment key from file.
    """
    load_dotenv()
    token = os.getenv("GITHUB_PAT")
    return token if token else None
