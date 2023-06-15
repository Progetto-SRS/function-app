import requests

# Controllo che il servizio check-name restituisca 'USATO'
response = requests.get("https://test-functions-srs.azurewebsites.net/api/check-name?nomeSito=teststoragesrs")
assert response.status_code == 200
assert response.content == b"USATO"

# Controllo che il servizio check-name restituisca 'SUCCESSO'
# Il nome del sito cambia in maniera tale da arrivare al successo del controllo
nomeSito = "testwebapp"
disponibilita = b"USATO"
while disponibilita == b"USATO":
    nomeSito += "srs"
    response = requests.get("https://test-functions-srs.azurewebsites.net/api/check-name?nomeSito=" + nomeSito)
    disponibilita = response.content
assert response.status_code == 200
assert response.content == b"SUCCESSO"

# Controllo che il servizio create-account-storage restituisca 'SUCCESSO'
gruppoRisorse = "test-env"
response = requests.get("https://test-functions-srs.azurewebsites.net/api/create-account-storage?nomeSito=" + nomeSito + "&gruppoRisorse=" + gruppoRisorse)
assert response.status_code == 200
assert response.content == b"SUCCESSO"

# Controllo che il servizio enable-static-website restituisca 'SUCCESSO'
response = requests.get("https://test-functions-srs.azurewebsites.net/api/enable-static-website?nomeSito=" + nomeSito)
assert response.status_code == 200
assert response.content == b"SUCCESSO"

# Controllo che il servizio delete-container restituisca 'SUCCESSO'
response = requests.get("https://test-functions-srs.azurewebsites.net/api/delete-container?nomeContainer=$web&accountStorage=" + nomeSito)
assert response.status_code == 200
assert response.content == b"SUCCESSO"
response = requests.get("https://" + nomeSito + ".z6.web.core.windows.net/")
assert response.status_code == 404
assert b"WebContentNotFound" in response.content

# Controllo che il servizio create-container restituisca 'SUCCESSO'
response = requests.get("https://test-functions-srs.azurewebsites.net/api/create-container?nomeContainer=$web&accountStorage=" + nomeSito)
assert response.status_code == 200
assert response.content == b"SUCCESSO"

# Controllo che il servizio copy-files restituisca 'SUCCESSO'
response = requests.get("https://test-functions-srs.azurewebsites.net/api/copy-files?nomeContainerOrigine=$web&accountStorageOrigine=teststoragesrs&nomeContainerDestinazione=$web&accountStorageDestinazione=" + nomeSito)
assert response.status_code == 200
assert response.content == b"SUCCESSO"
response = requests.get("https://" + nomeSito + ".z6.web.core.windows.net/")
assert response.status_code == 200
assert b"Sito prova" in response.content

# Controllo che il servizio disable-static-website restituisca 'SUCCESSO'
response = requests.get("https://test-functions-srs.azurewebsites.net/api/disable-static-website?nomeSito=" + nomeSito)
assert response.status_code == 200
assert response.content == b"SUCCESSO"
response = requests.get("https://" + nomeSito + ".z6.web.core.windows.net/")
assert response.status_code == 404
assert b"WebsiteDisabled" in response.content

# Controllo che il servizio delete-account-storage restituisca 'SUCCESSO'
response = requests.get("https://test-functions-srs.azurewebsites.net/api/delete-account-storage?nomeSito=" + nomeSito + "&gruppoRisorse=" + gruppoRisorse)
assert response.status_code == 200
assert response.content == b"SUCCESSO"