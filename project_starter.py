#!/home/kaiser/projects/project_starter/.venv/bin/python

import subprocess
import os
from pathlib import Path
import create_files
from load_env import get_github_key
from github_api import post_request
import json

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

    my_list = [add_command, commit_command, push_command]
    for command in my_list:
        if command.returncode != 0:
            print(f"Command: {command.args} result -> {command.stderr}")
            return False

    return True

#TODO: Get user input for this variables
token = "test"
repository_name = "test "
description = "test"

response = post_request(token, repository_name, description)
data = response.json()

repo_owner = data["owner"]["login"]
ssh_url = data["ssh_url"]
repo_name = data["name"]
print(repo_owner)
print(f"URL: {ssh_url}")
print("")
try:
    print("Attempting to clone repository!")
    subprocess_response = subprocess.run(
        ["git", "clone", ssh_url], check=True, capture_output=True, text=True
    )
    if subprocess_response.returncode == 0:
        print(f"Repository named: {repo_name} - was cloned successfully")

        os.chdir(repo_name)
        ##### CREATING FOLDER STRUCTURE AND FILES
        create_files.create_github_workflow(script_dir)
        create_files.create_git_ignore_file(script_dir)
        create_files.create_project_config_file(script_dir)
        create_files.create_requirements_file()
        create_files.create_readme_file(script_dir)

        #### COMMIT CHANGES TO REPO
        commit_response = commit_changes()
        print(f"Commit response: {commit_response}")

except subprocess.CalledProcessError as error:
    print(f"Command failed to run: {error.returncode}")
    print(f"Command error Response: {error.stderr}")
    print(f"Command error Response: {error.output}")
else:
data = response.json()
print(f"Error creating repository. Status code: {response.status_code}")
print(data["errors"])
