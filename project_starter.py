#!/home/kaiser/projects/project_starter/.venv/bin/python

import requests
import subprocess
import os
import create_files

from post_request_data import get_post_request_data
from commit_changes import commit_changes
from pathlib import Path

current_dir = Path(__file__).resolve().parent

while True:
    url, header, data = get_post_request_data()
    try:
        print("SENDING a POST request")
        print("")
        response = requests.post(url, headers=header, json=data)

        ##### GIT CLONE
        if response.status_code == 201:
            print("Repository Created successfully!")
            data = response.json()
            repo_owner = data["owner"]["login"]
            ssh_url = data["ssh_url"]
            repo_name = data["name"]
            print(f"username: {repo_owner}")
            print(f"Repo name: {repo_name}")
            print(f"URL: {ssh_url}")
            print("")

            try:
                print("Attempting to clone repository!")
                git_clone_response = subprocess.run(
                    ["git", "clone", ssh_url],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                if git_clone_response.returncode == 0:
                    print(f"Repository named: {repo_name} - was cloned successfully")
                    print("")

                    os.chdir(repo_name)
                    ##### CREATING FOLDER STRUCTURE AND FILES
                    create_files.create_git_ignore_file(current_dir)
                    create_files.create_github_workflow(current_dir)
                    create_files.create_project_config_file(current_dir)
                    create_files.create_requirements_file()
                    create_files.create_readme_file(current_dir)

                    #### COMMIT CHANGES TO REPO
                    commit_response = commit_changes()
                    if commit_response:
                        print("Changes committed succesfully.\n")
                        break
                    else:
                        print("An error occurred while commiting to repository.\n")

            except subprocess.CalledProcessError as error:
                print(f"Command failed to run: {error.returncode}")
                print(f"Command error Response: {error.stderr}")
                print(f"Command error Response: {error.output}")

        elif response.status_code == 422:
            print("Repository with same name already exists!\n")
            user_input = input("Would you like to try a new repository name? (y/n) \n")
            if user_input in ("yes" or "y"):
                continue
            else:
                print("Aborting script!!!!")
                break

        else:
            data = response.json()
            print(f"Error creating repository. Status code: {response.status_code}")
            print(data["errors"])
    except Exception as error:
        print("An error occurred while making a POST Request")
        print(f"Error -> {error}")
