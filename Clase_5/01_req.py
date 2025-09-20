import requests

url = "https://www.clarin.com"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    response = None

if response:
    print(response.status_code)

"""
1xx: Informational
2xx: Success
3xx: Redirection
4xx: Client Error
5xx: Server Error
"""    