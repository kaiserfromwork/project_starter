import shutil
from pathlib import Path


def create_github_workflow(dir_path: Path) -> None:
    github_workflow = dir_path / "configs" / "python_ci_config.yml"
    destination_file = Path(".github/workflows/python_ci.yml")

    try:
        print("Creating python-ci.yml file")
        destination_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(github_workflow, destination_file)
        print("Python CI configuration file created")
        print("")

    except IOError as error:
        print("An Error occurred while creating the file")
        print(f"Error: {error}")

    except Exception as error:
        print(f"An error occurred: {error}")


def create_readme_file(dir_path: Path) -> None:
    config_file = dir_path / "configs" / "readme_config.md"
    destination_file = "README.md"
    try:
        # shutil will create a copy of 'config_file' named 'README.md'. Since a absolute path wasn't provide
        # the file will be created locally.
        print("Creating README.md file")
        shutil.copyfile(config_file, destination_file)
        print("README.md file created successfully")
        print("")

    except IOError as error:
        print("An error occured while creating the file")
        print(f"Error: {error}")

    except Exception as error:
        print(f"An error occurred: {error}")


def create_requirements_file() -> None:
    destination_file = "requirements.txt"
    try:
        print(f"Creating {destination_file} file")
        with open(destination_file, "w") as file:
            file.write("")
        print(f"{destination_file} created successfully")
        print("")

    except IOError as error:
        print(f"An Error occurred while creating: {destination_file}")
        print(f"Error: {error}")

    except Exception as error:
        print(f"An error occurred: {error}")


def create_git_ignore_file(dir_path: Path) -> None:
    git_ignore_config = dir_path / "configs" / "git_ignore_config.txt"
    destinatio_file = ".gitignore"
    try:
        print("Creating '.gitignore' file")
        shutil.copyfile(git_ignore_config, destinatio_file)
        print(".gitignore file created successfully")
        print("")

    except IOError as error:
        print("An error occured while creating the file.")
        print(f"Error: {error}")

    except Exception as error:
        print(f"An error occurred: {error}")


def create_project_config_file(dir_path: Path) -> None:
    project_config_source = dir_path / "configs" / "project_config_file.toml"
    destination_file = "pyproject_config.toml"

    try:
        print(f"Creating {destination_file} file.")
        shutil.copyfile(project_config_source, destination_file)
        print(f"{destination_file} file created successfully.")
        print("")

    except IOError as error:
        print("An error occurred while creating file")
        print(f"Error: {error}")

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    print("Creating Files Script")
