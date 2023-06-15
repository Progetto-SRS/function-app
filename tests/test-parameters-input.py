import requests

response = requests.get("https://test-functions-srs.azurewebsites.net/api/check-name")
assert response.status_code == 400
assert response.content == b'ERRORE -> Manca il parametro nomeSito'

response = requests.get("https://test-functions-srs.azurewebsites.net/api/copy-files")
assert response.status_code == 400
assert response.content == b'ERRORE -> Mancano i parametri nomeContainerOrigine, accountStorageOrigine, nomeContainerDestinazione e accountStorageDestinazione'

response = requests.get("https://test-functions-srs.azurewebsites.net/api/create-account-storage")
assert response.status_code == 400
assert response.content == b'ERRORE -> Mancano i parametri nomeSito e gruppoRisorse'

response = requests.get("https://test-functions-srs.azurewebsites.net/api/create-container")
assert response.status_code == 400
assert response.content == b'ERRORE -> Mancano i parametri nomeContainer e accountStorage'

response = requests.get("https://test-functions-srs.azurewebsites.net/api/delete-account-storage")
assert response.status_code == 400
assert response.content == b'ERRORE -> Mancano i parametri nomeSito e gruppoRisorse'

response = requests.get("https://test-functions-srs.azurewebsites.net/api/delete-container")
assert response.status_code == 400
assert response.content == b'ERRORE -> Mancano i parametri nomeContainer e accountStorage'

response = requests.get("https://test-functions-srs.azurewebsites.net/api/disable-static-website")
assert response.status_code == 400
assert response.content == b'ERRORE -> Manca il parametro nomeSito'

response = requests.get("https://test-functions-srs.azurewebsites.net/api/enable-static-website")
assert response.status_code == 400
assert response.content == b'ERRORE -> Manca il parametro nomeSito'
