import requests

url = "https://test-functions-srs.azurewebsites.net/api/check-name"

response = requests.get(url)

assert response.status_code == 400