import subprocess


def commit_changes() -> bool:
    try:
        subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(["git", "push"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as error:
        print("An error occurred while commiting changes.\n")
        print(f"Error: {error}")
        return False

    except Exception as error:
        print("An unexpected error occurred while trying to commit to repository.\n")
        print(f"Error: {error}.")
        return False

    return True
