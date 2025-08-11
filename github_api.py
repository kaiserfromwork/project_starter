import requests


# POST Request
def post_request(
    token: str,
    repo_name: str,
    description: str = "this is my repository description",
    is_private: bool = False,
):
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

    try:
        print("Making a POST request")
        response = requests.post(url, headers=header, json=data)
        if response.status_code == 201:
            print("Repository created successfully!")
            return response
    except Exception as error:
        print("Error making POST request to GitHub API")
        print(f"Error: {error}")
