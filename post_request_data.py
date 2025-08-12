from load_env import get_github_key


def check_repo_name(repo_name: str) -> tuple:
    validation_errors = []
    if len(repo_name) > 100:
        validation_errors.append(
            "Repository name cannnot be longer than 100 characters"
        )
    if " " in repo_name:
        validation_errors.append("Blank space is not allowed when naming a repository")

    if not validation_errors:
        is_valid = True
    else:
        is_valid = False
    return (is_valid, validation_errors)


def get_post_request_data() -> tuple | None:
    repo_name = ""
    rename_repo = ""
    is_private = True

    token = get_github_key()
    if not token:
        print("PAT is not valid!")
        return None

    while True:
        repo_name = input("Please, enter a name for your repository. (No spaces)\n")
        result = check_repo_name(repo_name)
        if not result[0]:
            print("One or more errors occurred when naming the repository")
            print(result[1])
            print("")
            continue

        print(f"\nYour repository name is: {repo_name}")
        rename_repo = input("Please, confirm your repository name.\n")

        if rename_repo.lower() == repo_name.lower():
            description = input("Please, enter a description for the repository.\n")

            if description == "":
                description = "This is a repository"
                print("Your description was auto-generated\n")

            make_private = input("Would you like to your repository to be private?\n")
            if make_private.lower() in ("no", "n"):
                is_private = False
                print("Your repository was set to Public.\n")
            elif make_private.lower() in ("yes", "y"):
                is_private = True
                print("Your repository was set to Private.\n")
            else:
                print("Your repository was set to Private.\n")

        elif rename_repo.lower() not in repo_name.lower():
            print("Failed to confirm repository name.\nPlease, try again.\n")
            continue
        else:
            print("Invalid input. Please, try again.\n")
            continue

        break

    url = "https://api.github.com/user/repos"

    header = {
        "accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = {
        "name": f"{repo_name}",
        "description": f"{description}",
        "homepage": "https://github.com",
        "private": f"{is_private}",
        "is_template": True,
    }

    return url, header, data
