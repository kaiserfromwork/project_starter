import requests
import os
from dotenv import load_dotenv


def get_github_key() -> str | None:
    load_dotenv()
    GITHUB_TOKEN = os.getenv("GITHUB_PAT")

    return GITHUB_TOKEN


token = get_github_key()

url = "https://api.github.com/user/repos"

header = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28",
}
data = {
    "name": "Hello World",
    "description": "This is my first automated repository creation",
    "homepage": "https://github.com",
    "private": False,
    "is_template": True,
}

response = requests.post(url, headers=header, json=data)

if response.status_code == 201:
    print("Repository Created successfully!")
    print(response.json())
else:
    print(f"Error creating repository. Status code: {response.status_code}")
    print(response.text)
