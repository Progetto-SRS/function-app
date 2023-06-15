import requests

# Controllo che il servizio check-name restituisca 'USATO'
def test_1():
    esito = 503
    while esito == 503:
        response = requests.post("https://test-functions-srs.azurewebsites.net/api/check-name", json={"nomeSito": "teststoragesrs"})
        esito = response.status_code
    assert esito == 200
    assert response.content == b"USATO"

# Controllo che il servizio check-name restituisca 'SUCCESSO'
# Il nome del sito cambia in maniera tale da arrivare al successo del controllo
def test_2(nomeSito):
    esito = 503
    while esito == 503:
        disponibilita = b"USATO"
        while disponibilita == b"USATO":
            nomeSito += "srs"
            response = requests.post("https://test-functions-srs.azurewebsites.net/api/check-name", json={"nomeSito": nomeSito})
            disponibilita = response.content
            esito = response.status_code
    assert esito == 200
    assert disponibilita == b"DISPONIBILE"
    return nomeSito

# Controllo che il servizio create-account-storage restituisca 'SUCCESSO'
def test_3():
    esito = 503
    while esito == 503:
        response = requests.post("https://test-functions-srs.azurewebsites.net/api/create-account-storage", json={"nomeSito": nomeSito, "gruppoRisorse": gruppoRisorse})
        esito = response.status_code
    assert esito == 200
    assert response.content == b"SUCCESSO"
    
# Controllo che il servizio enable-static-website restituisca 'SUCCESSO'
def test_4():
    esito = 503
    while esito == 503:
        response = requests.post("https://test-functions-srs.azurewebsites.net/api/enable-static-website", json={"nomeSito": nomeSito})
        esito = response.status_code
    assert esito == 200
    assert response.content == b"SUCCESSO"

# Controllo che il servizio disable-static-website restituisca 'SUCCESSO'
def test_5():
    esito = 503
    while esito == 503:
        response = requests.post("https://test-functions-srs.azurewebsites.net/api/disable-static-website", json={"nomeSito": nomeSito})
        esito = response.status_code
    assert esito == 200
    assert response.content == b"SUCCESSO"

# Controllo che il servizio delete-account-storage restituisca 'SUCCESSO'
def test_6():
    esito = 503
    while esito == 503:
        response = requests.post("https://test-functions-srs.azurewebsites.net/api/delete-account-storage", json={"nomeSito": nomeSito, "gruppoRisorse": gruppoRisorse})
        esito = response.status_code
    assert esito == 200
    assert response.content == b"SUCCESSO"

nomeSito = "testwebapp"
gruppoRisorse = "test-env"

test_1()
nomeSito = test_2(nomeSito)
test_3()
test_4()
test_5()
test_6()