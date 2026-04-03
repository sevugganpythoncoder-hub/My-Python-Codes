# Getting info
# Weather
>>> def get_weather(city):
...     url = f"https://wttr.in/{city}?format=j1"
...     response = requests.get(url)
...     if response.status_code == 200:
...         temp = response.json()["current_condition"][0]["temp_C"]
...         return f"Tempereature in {city} : {temp}"
...     return f"Unavaliable for {city}"
>>> # Accessing Github
... def get_github_status(user):
...     url2 = f"https://api.github.com/users/{user}"
...     response2 = requests.get(url2)
...     if response2.status_code == 200:
...         data = response2.json().get("public_repos",0)
...         return f"Github Repos : {data}"
...     return "Github status Unavaliable"
  # Motivational quotes
... def get_quote():
...     url3 = "https://zenquotes.io/api/random"
...     response3 = requests.get(url3)
...     if response3.status_code == 200:
...         dump = response3.json()
...         quote = dump[0]["q"]
...         author = dump[0]["a"]
...         return f"{quote}-{author}"
...     return "Server Down : Offline"
... print(get_weather("Chennai"))
... print(get_github_status("sevugganpythoncoder-hub"))
... print(get_quote())
...
# OUTPUT:
Tempereature in Chennai : 32
Github Repos : 1
There are only two ways to live your life. One is as if nothing is a miracle. The other is as if everything is a miracle.-Albert Einstein
