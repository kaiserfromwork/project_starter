import os


def create_folders_and_files():
    # FOLDERS
    github_actions_folder = ".github/workflows"
    testing_folder = "tests"

    # MAKE DIRECTORIES
    os.makedirs(github_actions_folder, exist_ok=True)
    os.makedirs(testing_folder, exist_ok=True)

    # MAKE FILES
    github_actions_path = os.path.join(github_actions_folder, "python.yml")
    with open(github_actions_path, "w") as file:
        file.write("test")  # TODO: Change this to the actual file structure

    with open("README.md:q", "w") as file:
        file.write("test")  # TODO: Change this to the actual file structure

    with open(".gitignore", "w") as file:
        file.write("test")  # TODO: CHANGE THIS TO THE ACTUAL FILE

    with open("requirements.txt", "w") as file:
        file.write("test")  # TODO: CHANGE THIS TO THE ACTUAL FILE

    with open("pythonproject.toml", "w") as file:
        file.write("test")  # TODO: CHANGE THIS TO THE ACTUAL FILE
