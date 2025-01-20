import requests
repo_url="https://api.github.com/repos/OmoshJatelo/C-programing-assignments"
response=requests.get(repo_url)
print(response.json())