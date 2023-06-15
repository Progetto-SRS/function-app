import requests

# Controllo che il servizio create-container restituisca 'SUCCESSO'
def test_1():
    esito = 503
    while esito == 503:
        response = requests.post("https://test-functions-srs.azurewebsites.net/api/create-container", json={"nomeContainer": "testpipeline", "accountStorage": "teststoragesrs"})
        esito = response.status_code
    assert esito == 200
    assert response.content == b"SUCCESSO"

# Controllo che il servizio copy-files restituisca 'SUCCESSO'
def test_2():
    esito = 503
    while esito == 503:
        response = requests.post("https://test-functions-srs.azurewebsites.net/api/copy-files", json={"nomeContainerOrigine": "$web", "accountStorageOrigine": "teststoragesrs", "nomeContainerDestinazione": "testpipeline", "accountStorageDestinazione": "teststoragesrs"})
        esito = response.status_code
    assert esito == 200
    assert response.content == b"SUCCESSO"
    response = requests.get("https://teststoragesrs.blob.core.windows.net/testpipeline/index.html")
    assert response.status_code == 200
    assert b"Sito prova" in response.content


# Controllo che il servizio delete-container restituisca 'SUCCESSO'
def test_3():
    esito = 503
    while esito == 503:
        response = requests.post("https://test-functions-srs.azurewebsites.net/api/delete-container", json={"nomeContainer":"testpipeline", "accountStorage": "teststoragesrs"})
        esito = response.status_code
    assert esito == 200
    assert response.content == b"SUCCESSO"

test_1()
test_2()
test_3()