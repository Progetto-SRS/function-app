import requests

response = requests.get("https://test-functions-srs.azurewebsites.net/api/check-name")
assert response.status_code == 400
assert response.content == b"ERRORE -> Manca il parametro nomeSito"
print("Funzione check-name testata con successo...")

response = requests.get("https://test-functions-srs.azurewebsites.net/api/create-account-storage")
assert response.status_code == 400
assert response.content == b"ERRORE -> Mancano i parametri nomeSito e gruppoRisorse"
print("Funzione create-account-storage testata con successo...")

response = requests.get("https://test-functions-srs.azurewebsites.net/api/delete-account-storage")
assert response.status_code == 400
assert response.content == b"ERRORE -> Mancano i parametri nomeSito e gruppoRisorse"
print("Funzione delete-account-storage testata con successo...")

response = requests.get("https://test-functions-srs.azurewebsites.net/api/enable-static-website")
assert response.status_code == 400
assert response.content == b"ERRORE -> Manca il parametro nomeSito"
print("Funzione enable-static-website testata con successo...")

response = requests.get("https://test-functions-srs.azurewebsites.net/api/disable-static-website")
assert response.status_code == 400
assert response.content == b"ERRORE -> Manca il parametro nomeSito"
print("Funzione disable-static-website testata con successo...")