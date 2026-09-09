import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

# Imprimimos el resultado en la consola para poder verlo
print(response.json())