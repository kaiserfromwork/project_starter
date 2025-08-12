from load_env import get_github_key


def get_post_request_data() -> tuple:
    # TODO: Get user input to assign value to these variables
    token = get_github_key()
    repo_name = "Hello-World"
    description = "This is a repository"
    is_private = False

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
