import subprocess

response = subprocess.run(["git", "status"], check=True, capture_output=True, text=True)

print(response.stdout)
