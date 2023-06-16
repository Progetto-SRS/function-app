import requests
import time

# Controllo che il servizio create-container restituisca 'SUCCESSO'
response = requests.post("https://prod-functions-srs.azurewebsites.net/api/create-container", json={"nomeContainer": "testpipeline", "accountStorage": "prodstoragesrs"})
assert response.status_code == 200
assert response.content == b"SUCCESSO"
time.sleep(60)

# Controllo che il servizio copy-files restituisca 'SUCCESSO'
response = requests.post("https://prod-functions-srs.azurewebsites.net/api/copy-files", json={"nomeContainerOrigine": "$web", "accountStorageOrigine": "prodstoragesrs", "nomeContainerDestinazione": "testpipeline", "accountStorageDestinazione": "prodstoragesrs"})
assert response.status_code == 200
assert response.content == b"SUCCESSO"
response = requests.get("https://teststoragesrs.blob.core.windows.net/testpipeline/index.html")
assert response.status_code == 200
assert b"Sito prova" in response.content
time.sleep(60)

# Controllo che il servizio delete-container restituisca 'SUCCESSO'
response = requests.post("https://prod-functions-srs.azurewebsites.net/api/delete-container", json={"nomeContainer":"testpipeline", "accountStorage": "prodstoragesrs"})
assert response.status_code == 200
assert response.content == b"SUCCESSO"