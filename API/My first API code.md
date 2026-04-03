# Github data
import requests

city = "chennai"
url = "https://api.github.com/users/sevugganpythoncoder-hub"
print(f"Fetching Data from {city} using url...")
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    repos = data.get("public_repos", 0)
    bio = data.get("bio","No Bio set")
    print(f"Total Projects : {repos}")
    print(f"Bio : {bio}")
    if repos >= 5:
        print("Elite ARCHITECTURE!")
    else:
        print("Keep building!")
else:
    print(f"Error {response.status_code} : Profile not found")
