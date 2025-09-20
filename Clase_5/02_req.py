import requests

url = "http://www.httpbin.org/get"
arg = {"nombre": "Juan", "apellido": "Perez", "edad": 30}

try:
    response = requests.get(url, params=arg)
except Exception as e:
    print(f"An error occurred: {e}")
    response = None

if response:
    print(f"STATUS CODE:\n{response.status_code}")
    print("_" * 40)
    print(f"URL:\n{response.url}")
    print("_" * 40)
    print(f"JSON:\n{response.json()}")