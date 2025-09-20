import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    response = None

if response:
    users = response.json()
    for user in users:
        print(f"Name: {user['name']}, Email: {user['email']}")