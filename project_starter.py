#!/home/kaiser/projects/project_starter/.venv/bin/python

import requests
import subprocess
import os
from dotenv import load_dotenv

# TODO: CHANGE THE NAME OF THE FILE AND FUNCTION FOR SOMETHING CLEARER
from create_folders_files import create_folders_and_files


# TODO: Move this to a separate file that takes a string with name of the key you need from the .env file
def get_github_key() -> str | None:
    load_dotenv()
    GITHUB_TOKEN = os.getenv("GITHUB_PAT")

    return GITHUB_TOKEN


# TODO: Remove default value, this is only for testing:
def commit_changes(message: str = "This is a commit") -> bool:
    add_command = subprocess.run(
        ["git", "add", "."], check=True, capture_output=True, text=True
    )
    # TODO: ADD THE OPTION TO CREATE A CUSOTM MESSAGE
    message = "This is a commit!"
    commit_command = subprocess.run(
        ["git", "commit", "-m", message], check=True, capture_output=True, text=True
    )
    push_command = subprocess.run(
        ["git", "push"], check=True, capture_output=True, text=True
    )

    # TODO: Make a better check for invalid returncode
    if (
        add_command.returncode or commit_command.returncode or push_command.returncode
    ) != 0:
        print("COMMAND FAILED")
        return False
    return True


token = get_github_key()

# POST Requests
url = "https://api.github.com/user/repos"

header = {
    "accept": "application/vnd.github+json",
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

##### GIT CLONE

clone_url = ""  # TODO: Remove this when refactoring the code

if response.status_code == 201:
    print("Repository Created successfully!")
    data = response.json()
    repo_owner = data["owner"]["login"]
    clone_url = data["clone_url"]
    print(repo_owner)
else:
    print(f"Error creating repository. Status code: {response.status_code}")
    print(response.status_code)

try:
    print("Attempting to run a command on the CLI")
    subprocess_response = subprocess.run(
        ["git", "clone", clone_url], check=True, capture_output=True, text=True
    )
    if subprocess_response.returncode == 0:
        print("Repository was cloneed successfully")

except subprocess.CalledProcessError as error:
    print(f"Command failed to run: {error.returncode}")
    print(f"Command error Response: {error.stderr}")
    print(f"Command error Response: {error.output}")

##### CREATING FOLDER STRUCTURE AND FILES
create_folders_and_files()

#### COMMIT CHANGES TO REPO

commit_response = commit_changes()
print(f"Commit response: {commit_response}")
