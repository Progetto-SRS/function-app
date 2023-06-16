import requests
import time

nomeSito = "testwebapp"
gruppoRisorse = "users-env"

# Controllo che il servizio check-name restituisca 'USATO'
response = requests.post("https://prod-functions-srs.azurewebsites.net/api/check-name", json={"nomeSito": "teststoragesrs"})
assert response.status_code == 200
assert response.content == b"USATO"

# Controllo che il servizio check-name restituisca 'SUCCESSO'
# Il nome del sito cambia in maniera tale da arrivare al successo del controllo
disponibilita = b"USATO"
while disponibilita == b"USATO":
    nomeSito += "srs"
    response = requests.post("https://prod-functions-srs.azurewebsites.net/api/check-name", json={"nomeSito": nomeSito})
    disponibilita = response.content
assert response.status_code == 200
assert disponibilita == b"DISPONIBILE"

# Controllo che il servizio create-account-storage restituisca 'SUCCESSO'
response = requests.post("https://prod-functions-srs.azurewebsites.net/api/create-account-storage", json={"nomeSito": nomeSito, "gruppoRisorse": gruppoRisorse})
assert response.status_code == 200
assert response.content == b"SUCCESSO"
time.sleep(60)

# Controllo che il servizio enable-static-website restituisca 'SUCCESSO'
response = requests.post("https://prod-functions-srs.azurewebsites.net/api/enable-static-website", json={"nomeSito": nomeSito})
assert response.status_code == 200
assert response.content == b"SUCCESSO"
time.sleep(60)

# Controllo che il servizio disable-static-website restituisca 'SUCCESSO'
response = requests.post("https://prod-functions-srs.azurewebsites.net/api/disable-static-website", json={"nomeSito": nomeSito})
assert response.status_code == 200
assert response.content == b"SUCCESSO"
time.sleep(60)

# Controllo che il servizio delete-account-storage restituisca 'SUCCESSO'
response = requests.post("https://prod-functions-srs.azurewebsites.net/api/delete-account-storage", json={"nomeSito": nomeSito, "gruppoRisorse": gruppoRisorse})
assert response.status_code == 200
assert response.content == b"SUCCESSO"