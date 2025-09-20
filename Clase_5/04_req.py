import requests
import json

url = "https://country.io/capital.json"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    response = None

if response:
    data = response.json()
    for elemento in data:
        print(f"{data[elemento]}")