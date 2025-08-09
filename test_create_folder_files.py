import os

github_actions_folder = ".github/workflows"

requirements = "requirements.txt"
actions_setup_file = "python.yml"
gitignore_file = ".gitignore"
build_config_file = "pythonproject.toml"
readme_file = "README.md"

test_folder = "test"
test_file = "test_file.txt"

test_path = os.path.join(test_folder, test_file)

os.makedirs(test_folder, exist_ok=True)
os.makedirs(github_actions_folder, exist_ok=True)


# with open(test_path, "w") as file:
#     file.write("This is a new file directory")
