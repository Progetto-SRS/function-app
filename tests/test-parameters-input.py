import requests

response = requests.get("https://test-functions-srs.azurewebsites.net/api/check-name")
assert response.status_code == 400