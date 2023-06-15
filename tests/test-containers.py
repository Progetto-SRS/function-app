import requests

# Controllo che il servizio create-container restituisca 'SUCCESSO'
response = requests.post("https://test-functions-srs.azurewebsites.net/api/create-container", json={"nomeContainer": "testpipeline", "accountStorage": "teststoragesrs"})
assert response.status_code == 200
assert response.content == b"SUCCESSO"

# Controllo che il servizio copy-files restituisca 'SUCCESSO'
response = requests.post("https://test-functions-srs.azurewebsites.net/api/copy-files", json={"nomeContainerOrigine": "$web", "accountStorageOrigine": "teststoragesrs", "nomeContainerDestinazione": "testpipeline", "accountStorageDestinazione": "teststoragesrs"})
assert response.status_code == 200
assert response.content == b"SUCCESSO"
response = requests.get("https://teststoragesrs.blob.core.windows.net/testpipeline/index.html")
assert response.status_code == 200
assert b"Sito prova" in response.content


# Controllo che il servizio delete-container restituisca 'SUCCESSO'
response = requests.post("https://test-functions-srs.azurewebsites.net/api/delete-container", json={"nomeContainer":"testpipeline", "accountStorage": "teststoragesrs"})
assert response.status_code == 200
assert response.content == b"SUCCESSO"