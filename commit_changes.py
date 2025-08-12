import subprocess


def commit_changes() -> bool:
    message = input("Please, enter your commit message.\n")

    add_command = subprocess.run(
        ["git", "add", "."], check=True, capture_output=True, text=True
    )
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
