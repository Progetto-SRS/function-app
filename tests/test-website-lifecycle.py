import requests

# Controllo che il servizio check-name restituisca 'USATO'
def test_1():
    esito = 503
    while esito == 503:
        response = requests.get("https://test-functions-srs.azurewebsites.net/api/check-name?nomeSito=teststoragesrs")
        esito = response.status_code
        print("1 - "+esito)
    assert esito == 200
    assert response.content == b"USATO"

# Controllo che il servizio check-name restituisca 'SUCCESSO'
# Il nome del sito cambia in maniera tale da arrivare al successo del controllo
def test_2():
    esito = 503
    while esito == 503:
        disponibilita = b"USATO"
        while disponibilita == b"USATO":
            nomeSito += "srs"
            response = requests.get("https://test-functions-srs.azurewebsites.net/api/check-name?nomeSito=" + nomeSito)
            disponibilita = response.content
            esito = response.status_code
            print("2 - "+esito)
    assert esito == 200
    assert disponibilita == b"DISPONIBILE"

# Controllo che il servizio create-account-storage restituisca 'SUCCESSO'
def test_3():
    esito = 503
    while esito == 503:
        response = requests.get("https://test-functions-srs.azurewebsites.net/api/create-account-storage?nomeSito=" + nomeSito + "&gruppoRisorse=" + gruppoRisorse)
        esito = response.status_code
        print("3 - "+esito)
    assert esito == 200
    assert response.content == b"SUCCESSO"
    
# Controllo che il servizio enable-static-website restituisca 'SUCCESSO'
def test_4():
    esito = 503
    while esito == 503:
        response = requests.get("https://test-functions-srs.azurewebsites.net/api/enable-static-website?nomeSito=" + nomeSito)
        esito = response.status_code
        print("4 - "+esito)
    assert esito == 200
    assert response.content == b"SUCCESSO"

# Controllo che il servizio delete-container restituisca 'SUCCESSO'
def test_5():
    esito = 503
    while esito == 503:
        response = requests.get("https://test-functions-srs.azurewebsites.net/api/delete-container?nomeContainer=$web&accountStorage=" + nomeSito)
        esito = response.status_code
        print("5 - "+esito)
    assert esito == 200
    assert response.content == b"SUCCESSO"
    response = requests.get("https://" + nomeSito + ".z6.web.core.windows.net/")
    assert response.status_code == 404
    assert b"WebContentNotFound" in response.content

# Controllo che il servizio create-container restituisca 'SUCCESSO'
def test_6():
    esito = 503
    while esito == 503:
        response = requests.get("https://test-functions-srs.azurewebsites.net/api/create-container?nomeContainer=$web&accountStorage=" + nomeSito)
        esito = response.status_code
        print("6 - "+esito)
    assert esito == 200
    assert response.content == b"SUCCESSO"

# Controllo che il servizio copy-files restituisca 'SUCCESSO'
def test_7():
    esito = 503
    while esito == 503:
        response = requests.get("https://test-functions-srs.azurewebsites.net/api/copy-files?nomeContainerOrigine=$web&accountStorageOrigine=teststoragesrs&nomeContainerDestinazione=$web&accountStorageDestinazione=" + nomeSito)
        esito = response.status_code
        print("7 - "+esito)
    assert esito == 200
    assert response.content == b"SUCCESSO"
    response = requests.get("https://" + nomeSito + ".z6.web.core.windows.net/")
    assert response.status_code == 200
    assert b"Sito prova" in response.content

# Controllo che il servizio disable-static-website restituisca 'SUCCESSO'
def test_8():
    esito = 503
    while esito == 503:
        response = requests.get("https://test-functions-srs.azurewebsites.net/api/disable-static-website?nomeSito=" + nomeSito)
        esito = response.status_code
        print("8 - "+esito)
    assert esito == 200
    assert response.content == b"SUCCESSO"
    response = requests.get("https://" + nomeSito + ".z6.web.core.windows.net/")
    assert response.status_code == 404
    assert b"WebsiteDisabled" in response.content

# Controllo che il servizio delete-account-storage restituisca 'SUCCESSO'

def test_9():
    esito = 503
    while esito == 503:
        response = requests.get("https://test-functions-srs.azurewebsites.net/api/delete-account-storage?nomeSito=" + nomeSito + "&gruppoRisorse=" + gruppoRisorse)
        esito = response.status_code
        print("9 - "+esito)
    assert esito == 200
    assert response.content == b"SUCCESSO"

nomeSito = "testwebapp"
gruppoRisorse = "test-env"

test_1()
test_2()
test_3()
test_4()
test_5()
test_6()
test_7()
test_8()
test_9()