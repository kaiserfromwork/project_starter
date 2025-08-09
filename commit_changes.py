import subprocess


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
